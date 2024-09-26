import random
from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
from pyspark.sql.functions import udf, col
from pyspark.sql.types import StringType, IntegerType
import random

spark = SparkSession \
        .builder \
        .master("local[*]") \
        .appName("Exercicio Intro") \
        .getOrCreate()

print(f'Etapa 1 - Leitura do arquivo')
df_nomes = spark.read.csv('../1-spark-batch/nomes_aleatorios.txt')

print(f'Arquivo lido com sucesso!\n')

df_nomes.printSchema()

##################################################

print(f'\nEtapa 2 - Renomeação da coluna para "nomes"')
df_nomes = df_nomes.withColumnRenamed('_c0', 'nomes')

print("Coluna renomeada com sucesso!")

df_nomes.printSchema()

###############################################

print(f'\nEtapa 3 - Inserir coluna "Escolaridade"')

def escolher_escolaridade():
    return random.choice(['Fundamental', 'Medio', 'Superior'])

escolher_escolaridade_udf = udf(escolher_escolaridade, StringType())

df_nomes = df_nomes.withColumn("Escolaridade", escolher_escolaridade_udf())

print(f'Escolaridades inseridas com sucesso!\n')

df_nomes.show(10)

#################################################

# Etapa 4
print(f'\nEtapa 4 - Inserir coluna "Pais"')

def escolher_pais():
    return random.choice(["Argentina", "Bolívia", "Brasil", "Chile", "Colômbia", "Equador", "Guiana", 
          "Guiana Francesa", "Paraguai", "Peru", "Suriname", "Uruguai", "Venezuela"])

escolher_pais_udf = udf(escolher_pais, StringType())

df_nomes = df_nomes.withColumn("Pais", escolher_pais_udf())

print(f'Paises inseridos com sucesso!\n')

df_nomes.show(10)

#####################################################

# Etapa 5
print(f'\nEtapa 5 - Inserir coluna "AnoNascimento"')

def escolher_ano_nascimento():
    return random.randint(1945, 2010)

escolher_ano_nascimento_udf = udf(escolher_ano_nascimento, IntegerType())
df_nomes = df_nomes.withColumn("AnoNascimento", escolher_ano_nascimento_udf())

print(f'Anos de nascimento inseridos com sucesso!\n')

df_nomes.show(10)

###########################################################

# Etapa 6

df_nomes = df_nomes.cache()

print(f'\nEtapa 6 - Filtrar pessoas que nasceram no seculo XXI')

df_select = df_nomes.filter(col("AnoNascimento") >= 2000).select('nomes', 'AnoNascimento')

df_select.show(10)

# Etapa 7

print(f'\nEtapa 7 - Filtrar pessoas que nasceram no seculo XXI com SparkSQL')

df_nomes.createOrReplaceTempView("pessoas")

spark.sql("SELECT nomes, AnoNascimento FROM pessoas WHERE AnoNascimento >= 2000").show(10)


# Etapa 8
print(f'\nEtapa 8 - Total de pessoas Millenials (que nasceram entre 1980 e 1994)')

df_millenials = df_nomes.filter((col("AnoNascimento") >= 1980) &(col("AnoNascimento") <= 1994)).select('nomes', 'AnoNascimento')

print(f'Quantidade de pessoas "Millenials" {df_millenials.count()}')

# Etapa 9
print(f'\nEtapa 9 - Total de pessoas Millenials com Spark SQL')

spark.sql("SELECT count(*) as total_millennials FROM pessoas WHERE AnoNascimento >= 1980 AND AnoNascimento <= 1994").show()


# Etapa 10
print(f'\nEtapa 10 - Consulta e contagem por geração e pais')

query = """
SELECT 
    Pais,
    CASE 
        WHEN AnoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
        WHEN AnoNascimento BETWEEN 1965 AND 1979 THEN 'Geração X'
        WHEN AnoNascimento BETWEEN 1980 AND 1994 THEN 'Millenials'
        WHEN AnoNascimento BETWEEN 1995 AND 2015 THEN 'Geração Z'
        ELSE 'Outras'
    END AS Geracao,
    COUNT(*) AS Quantidade
FROM pessoas
GROUP BY Pais, Geracao
ORDER BY Pais, Geracao, Quantidade
"""

df_resultado = spark.sql(query)

df_resultado.show()
