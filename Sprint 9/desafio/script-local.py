from pyspark.sql import SparkSession

# Cria uma sessão do Spark
spark = SparkSession.builder \
    .appName("Ler Arquivos Parquet em Diretório") \
    .getOrCreate()

# Define o caminho para o diretório que contém os arquivos Parquet
caminho_diretorio = "TMDB/"

# Lê todos os arquivos Parquet do diretório e cria um DataFrame
df = spark.read.parquet(caminho_diretorio)

print(f'Arquivos locais - CSV')

# Exibe o esquema do DataFrame
df.printSchema()

# Exibe as primeiras linhas do DataFrame
#df.show()

caminho_diretorio = "Local/"

df = spark.read.parquet(caminho_diretorio)

print(f'Arquivos TMDB - JSON')

df.printSchema()

# Encerra a sessão Spark
spark.stop()
