from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_replace, col

# Cria uma sessão do Spark
spark = SparkSession.builder \
    .appName("Ler Arquivos Parquet em Diretório") \
    .getOrCreate()


# Define o caminho para o diretório que contém os arquivos Parquet do CSV (Local)
caminho_diretorio_csv = "Local/"

# Lê todos os arquivos Parquet do diretório Local e cria um DataFrame
df_csv = spark.read.parquet(caminho_diretorio_csv)

print(f'Arquivos locais - CSV')
df_csv.printSchema()

# Define o caminho para o diretório que contém os arquivos Parquet do JSON (TMDB)
caminho_diretorio_tmdb = "TMDB/"

# Lê todos os arquivos Parquet do diretório TMDB e cria um DataFrame
df_tmdb = spark.read.parquet(caminho_diretorio_tmdb)

print(f'Arquivos TMDB - JSON')
df_tmdb.printSchema()

df_csv = df_csv.drop("id")

# Converte o campo 'id' para o tipo long no DataFrame TMDB (se necessário)
df_tmdb = df_tmdb.withColumn("id", col("id").cast("long"))

# Faz a junção dos DataFrames utilizando o campo 'id' como chave
df_unido = df_csv.join(df_tmdb, df_csv.tituloPincipal == df_tmdb.titulo, "inner")

df_unido = df_unido.drop("popularidade").drop("anoLancamento").drop("tituloOriginal").drop("tituloPincipal").dropDuplicates(["id"])

# Exibe o esquema do DataFrame resultante
df_unido.printSchema()

# Exibe as primeiras linhas do DataFrame unido
df_unido.show()




# Encerra a sessão Spark
spark.stop()


