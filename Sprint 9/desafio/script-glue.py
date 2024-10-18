import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as F
from pyspark.sql.functions import col, split, explode, trim, year, month, dayofmonth, monotonically_increasing_id

# @params: [JOB_NAME, S3_INPUT_PATH, S3_TARGET_PATH]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

# Inicialização do contexto do Glue
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']  # Caminho de entrada (Raw Zone)
target_path = args['S3_TARGET_PATH']  # Caminho de saída (Trusted Zone)

df_csv = spark.read.parquet(f'{source_file}/Local/PARQUET/2024/10/03')
df_tmdb = spark.read.parquet(f'{source_file}/TMDB/PARQUET/data_criacao=2024-10-17')

# Remoção da coluna 'id' do DataFrame TMDB
df_tmdb = df_tmdb.drop("id")

# Faz a junção dos DataFrames utilizando o campo 'id' como chave
df_unido = df_csv.join(df_tmdb, df_csv.id == df_tmdb.id_imdb, "inner")

# Remove colunas desnecessárias e duplicatas por 'id'
df_unido = df_unido.drop("id_imdb").drop("tituloPincipal").drop("tituloOriginal").drop("anoLancamento").dropDuplicates(["id"])

# Criação campos ano, mês, dia e id_fato_filme
df_unido = df_unido.withColumn("ano", year(col("data_lancamento"))) \
                   .withColumn("mes", month(col("data_lancamento"))) \
                   .withColumn("dia", dayofmonth(col("data_lancamento"))) \
                   .withColumn("id_fato_filme", monotonically_increasing_id())

# Exibe o esquema do DataFrame unido
df_unido.printSchema()

target_path_movies = f'{target_path}/Movies'

# === 1. Tabela dim_titulo === #
dim_titulo = df_unido.select("id", "titulo")
dim_titulo.write \
    .format("parquet") \
    .mode("overwrite") \
    .save(f'{target_path_movies}/dim_titulo')
    
dim_titulo.show()

# === 2. Tabela dim_tempo === #
dim_tempo = df_unido.select("data_lancamento", "ano", "mes", "dia").distinct() \
                    .withColumn("id_tempo", monotonically_increasing_id())
                    
dim_tempo = dim_tempo.select("id_tempo", "data_lancamento", "ano", "mes", "dia")

dim_tempo.write \
    .format("parquet") \
    .mode("append") \
    .save(f'{target_path_movies}/dim_tempo')

dim_tempo.show()


# === 3. Tabela dim_diretor === #
dim_diretor = df_unido.select("diretor").distinct() \
    .withColumn("id_diretor", monotonically_increasing_id())

dim_diretor = dim_diretor.select("id_diretor", "diretor")  

dim_diretor.write \
    .format("parquet") \
    .mode("append") \
    .save(f'{target_path_movies}/dim_diretor')
    
dim_diretor.show()


# === 4. Tabela dim_genero === #
# Explodir o campo 'genero' para ter uma linha por gênero e criar IDs únicos
df_genero_exploded = df_unido.withColumn("genero", explode(split(col("genero"), ","))) \
                             .withColumn("genero", trim(col("genero")))  # Remove espaços extras

# Seleciona o campo 'genero' e cria um ID único
dim_genero = df_genero_exploded.select("genero").distinct() \
                               .withColumn("id_genero", monotonically_increasing_id())

dim_genero = dim_genero.select("id_genero", "genero")  


dim_genero.write \
    .format("parquet") \
    .mode("append") \
    .save(f'{target_path_movies}/dim_genero')
    

dim_genero.show()


# === 5. Tabela fato_filme === #
# Unir a tabela principal com as dimensões (diretor, tempo e título)
fato_filme = df_unido.join(dim_diretor, on="diretor", how="left") \
                     .join(dim_tempo, on=["ano", "mes", "dia"], how="left") \
                     .join(dim_titulo, on="id", how="left") \
                     .withColumn("id_fato_filme", monotonically_increasing_id()) \
                     .select("id_fato_filme", "notaMedia", "popularidade", "numeroVotos", "orcamento", "receita", 
                             "id", "id_tempo", "id_diretor")
fato_filme.write \
    .format("parquet") \
    .mode("append") \
    .save(f'{target_path_movies}/fato_filme')        

fato_filme.show()
                             

# === 6. Tabela de Ponte (filme - genero) === #
# Criar a tabela de ponte entre filme e gênero, utilizando os IDs das tabelas correspondentes
tabela_ponte_filme_genero = df_genero_exploded.join(fato_filme, on="id_fato_filme", how="left") \
                                              .join(dim_genero, on="genero", how="left") \
                                              .select("id_fato_filme", "id_genero") \
                                              .distinct()                             
tabela_ponte_filme_genero.write \
    .format("parquet") \
    .mode("append") \
    .save(f'{target_path_movies}/filme_genero')


tabela_ponte_filme_genero.show()

# Finaliza o job
job.commit()