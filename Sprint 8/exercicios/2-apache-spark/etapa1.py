from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext

spark = SparkSession \
        .builder \
        .master("local[*]") \
        .appName("Exercicio Intro") \
        .getOrCreate()

df_nomes = spark.read.csv('../1-spark-batch/nomes_aleatorios.txt')

df_nomes.show(5)