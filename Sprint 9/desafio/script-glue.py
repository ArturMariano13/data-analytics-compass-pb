import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as F
from pyspark.sql.functions import col

# @params: [JOB_NAME, S3_INPUT_PATH, S3_TARGET_PATH]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

# Inicialização do contexto do Glue
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']  # Caminho de entrada (Trusted Zone)
target_path = args['S3_TARGET_PATH']  # Caminho de saída (Refined Zone)

df_csv = spark.read.parquet(f'{source_file}/Local/PARQUET/2024/10/03')
df_tmdb = spark.read.parquet(f'{source_file}/TMDB/PARQUET/data_criacao=2024-09-23')

# Remoção da coluna 'id' do DataFrame CSV e conversão do 'id' em TMDB para long
df_csv = df_csv.drop("id")
df_tmdb = df_tmdb.withColumn("id", col("id").cast("long"))

# Faz a junção dos DataFrames
df_unido = df_csv.join(df_tmdb, df_csv.tituloPincipal == df_tmdb.titulo, "inner")

# Remove colunas desnecessárias e duplicatas por 'id'
df_unido = df_unido.drop("popularidade", "anoLancamento", "tituloOriginal", "tituloPincipal") \
                   .dropDuplicates(["id"])

# Exibe o esquema do DataFrame unido
df_unido.printSchema()

target_path_movies = f'{target_path}/Movies'

# 1. Tabela fato_filme
fato_filme = df_unido.select("id", "numeroVotos", "notaMedia", "orcamento", "receita")
fato_filme.write \
    .format("parquet") \
    .mode("overwrite") \
    .save(f'{target_path_movies}/fato_filme')

# 2. Tabela dim_titulo
dim_titulo = df_unido.select("id", "titulo")
dim_titulo.write \
    .format("parquet") \
    .mode("append") \
    .save(f'{target_path_movies}/dim_titulo')

# 3. Tabela dim_tempo (extraindo ano, mês e dia de 'dataLancamento')
df_unido = df_unido.withColumn("ano", col("data_lancamento").substr(1, 4)) \
                   .withColumn("mes", col("data_lancamento").substr(6, 2)) \
                   .withColumn("dia", col("data_lancamento").substr(9, 2))

dim_tempo = df_unido.select("id", "data_lancamento", "ano", "mes", "dia")
dim_tempo.write \
    .format("parquet") \
    .mode("append") \
    .save(f'{target_path_movies}/dim_tempo')

# 4. Tabela dim_genero
dim_genero = df_unido.select("id", "genero")
dim_genero.write \
    .format("parquet") \
    .mode("append") \
    .save(f'{target_path_movies}/dim_genero')

# === 5. Validação e criação da tabela dim_diretor === #
# Verifica se a coluna 'produtoras' existe e se contém valores
if 'produtoras' in df_unido.columns and df_unido.filter(F.col("produtoras").isNotNull()).count() > 0:
    # Define o valor do diretor como 'Christopher Nolan' quando há produtoras
    dim_diretor = df_unido.withColumn("diretor", F.lit("Christopher Nolan")) \
                          .select("id", "diretor")

dim_diretor.write \
    .format("parquet") \
    .mode("append") \
    .save(f'{target_path_movies}/dim_diretor')

# Finaliza o job
job.commit()