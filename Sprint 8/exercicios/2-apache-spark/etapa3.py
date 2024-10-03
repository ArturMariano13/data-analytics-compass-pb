import random
from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
import random

spark = SparkSession \
        .builder \
        .master("local[*]") \
        .appName("Exercicio Intro") \
        .getOrCreate()

df_nomes = spark.read.csv('../1-spark-batch/nomes_aleatorios.txt')

# Etapa 2
df_nomes = df_nomes.withColumnRenamed('_c0', 'nomes')

# Etapa 3
def escolher_escolaridade():
    return random.choice(['Fundamental', 'Medio', 'Superior'])

escolher_escolaridade_udf = udf(escolher_escolaridade, StringType())

df_nomes = df_nomes.withColumn("Escolaridade", escolher_escolaridade_udf())

df_nomes.show(10)