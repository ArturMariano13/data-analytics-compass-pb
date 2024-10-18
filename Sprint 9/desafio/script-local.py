import sys
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.functions import col, split, explode, year, month, dayofmonth, monotonically_increasing_id

# Inicialização do Spark
sc = SparkContext()
spark = SparkSession(sc)

# Substitua esses caminhos pelos seus arquivos locais para teste
source_file_local = 'Local'
source_file_tmdb = 'parquet'

# Leitura dos arquivos de entrada em formato Parquet (ajuste os caminhos conforme necessário)
df_csv = spark.read.parquet(source_file_local)
df_tmdb = spark.read.parquet(source_file_tmdb)

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


# === 1. Tabela dim_titulo === #
dim_titulo = df_unido.select("id", "titulo")

print("Tabela dim_titulo")
dim_titulo.show(truncate=False)


# === 2. Tabela dim_tempo === #
dim_tempo = df_unido.select("data_lancamento", "ano", "mes", "dia").distinct() \
                    .withColumn("id_tempo", monotonically_increasing_id())

print("Tabela dim_tempo")
dim_tempo.show(truncate=False)

# === 3. Tabela dim_diretor === #
dim_diretor = df_unido.select("diretor").distinct() \
                          .withColumn("id_diretor", monotonically_increasing_id())

print("Tabela Dimensão Diretor (IDs Únicos):")
dim_diretor.show(truncate=False)

# === 4. Tabela dim_genero === #
# Explodir o campo 'genero' para ter uma linha por gênero e criar IDs únicos
df_genero_exploded = df_unido.withColumn("genero", explode(split(col("genero"), ","))) \
                             .withColumn("genero", F.trim(col("genero")))  # Remove espaços extras

dim_genero = df_genero_exploded.select("genero").distinct() \
                               .withColumn("id_genero", monotonically_increasing_id())

print("Tabela Dimensão Gênero:")
dim_genero.show(truncate=False)


# === 5. Tabela fato_filme === #
# Unir a tabela principal com as dimensões (diretor, tempo e título)
fato_filme = df_unido.join(dim_diretor, on="diretor", how="left") \
                     .join(dim_tempo, on=["ano", "mes", "dia"], how="left") \
                     .join(dim_titulo, on="id", how="left") \
                     .withColumn("id_fato_filme", monotonically_increasing_id()) \
                     .select("id_fato_filme", "notaMedia", "popularidade", "numeroVotos", "orcamento", "receita", 
                             "id", "id_tempo", "id_diretor")

print("Tabela Fato Filme:")
fato_filme.printSchema()

# === 6. Tabela de Ponte (filme - genero) === #
# Criar a tabela de ponte entre filme e gênero, utilizando os IDs das tabelas correspondentes
tabela_ponte_filme_genero = df_genero_exploded.join(fato_filme, on="id_fato_filme", how="left") \
                                              .join(dim_genero, on="genero", how="left") \
                                              .select("id_fato_filme", "id_genero") \
                                              .distinct()

print("Tabela de Ponte (Filme - Gênero):")
tabela_ponte_filme_genero.show(truncate=False)


# Finaliza o SparkContext
sc.stop()
