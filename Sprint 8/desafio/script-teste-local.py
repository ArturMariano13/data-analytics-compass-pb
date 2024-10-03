from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import IntegerType, FloatType

# 1. Criando uma sessão Spark local
spark = SparkSession.builder \
    .appName("FilmesProcessingLocal") \
    .getOrCreate()

# 2. Leitura dos dados a partir de um arquivo CSV
source_file = "movies.csv"  # Altere para o caminho do seu arquivo local
df_spark = spark.read \
    .option("header", True) \
    .option("sep", "|") \
    .csv(source_file)

# 3. Converter colunas para os tipos apropriados
df_spark = df_spark.withColumn("anoLancamento", F.col("anoLancamento").cast(IntegerType())) \
                   .withColumn("notaMedia", F.col("notaMedia").cast(FloatType())) \
                   .withColumn("numeroVotos", F.col("numeroVotos").cast(IntegerType()))

# 4. Selecionar colunas de interesse
df_selected = df_spark.select("id", "tituloPincipal", "tituloOriginal", "anoLancamento", 
                              "genero", "notaMedia", "numeroVotos")

# 5. Buscar todos os filmes em que Heath Ledger atuou
df_heath_ledger = df_spark.filter(F.col("nomeArtista").contains("Heath Ledger"))

# 6. Buscar filmes lançados entre 2000 e 2020
df_filmes_2000_2020 = df_selected.filter((F.col("anoLancamento") >= 2000) & 
                                         (F.col("anoLancamento") <= 2020))

# 7. Remover duplicados pelo id
df_deduplicated = df_filmes_2000_2020.dropDuplicates(["id"])

# 8. Mostrar os DataFrames na tela
print("Filmes de Heath Ledger:")
df_heath_ledger.show(truncate=False)

print("Filmes lançados entre 2000 e 2020 sem duplicatas:")
df_deduplicated.show(truncate=False)

# Finalizar a sessão Spark
spark.stop()