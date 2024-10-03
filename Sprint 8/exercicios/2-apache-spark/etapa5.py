import random
from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType, IntegerType
import random

spark = SparkSession \
        .builder \
        .master("local[*]") \
        .appName("Exercicio Intro") \
        .getOrCreate()

# Etapa 1
df_nomes = spark.read.csv('../1-spark-batch/nomes_aleatorios.txt')

# Etapa 2
df_nomes = df_nomes.withColumnRenamed('_c0', 'nomes')

# Etapa 3
def escolher_escolaridade():
    return random.choice(['Fundamental', 'Medio', 'Superior'])

escolher_escolaridade_udf = udf(escolher_escolaridade, StringType())

df_nomes = df_nomes.withColumn("Escolaridade", escolher_escolaridade_udf())

# Etapa 4
def escolher_pais():
    return random.choice(["Argentina", "Bolívia", "Brasil", "Chile", "Colômbia", "Equador", "Guiana", 
          "Guiana Francesa", "Paraguai", "Peru", "Suriname", "Uruguai", "Venezuela"])

escolher_pais_udf = udf(escolher_pais, StringType())

df_nomes = df_nomes.withColumn("Pais", escolher_pais_udf())


# Etapa 5
def escolher_ano_nascimento():
    return random.randint(1945, 2010)

escolher_ano_nascimento_udf = udf(escolher_ano_nascimento, IntegerType())
df_nomes = df_nomes.withColumn("AnoNascimento", escolher_ano_nascimento_udf())


df_nomes.show(10)