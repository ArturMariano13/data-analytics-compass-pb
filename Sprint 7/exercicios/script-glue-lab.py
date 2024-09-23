import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as F
from pyspark.sql.types import IntegerType  # Adicionando o tipo numérico

# @params: [JOB_NAME, S3_INPUT_PATH, S3_TARGET_PATH]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Paths
source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

# 1. Lendo o arquivo nomes.csv do S3
df_dynamic = glueContext.create_dynamic_frame.from_options(
    "s3",
    {
        "paths": [source_file]
    },
    "csv",
    {"withHeader": True, "separator": ","},
)

# Convertendo para um DataFrame Spark
df_spark = df_dynamic.toDF()

# 2. Imprimindo o schema original
df_spark.printSchema()

# 3. Alterando a caixa dos valores da coluna 'nome' para maiúsculo
df_spark = df_spark.withColumn('nome', F.upper(F.col('nome')))

# 3.1. Convertendo as colunas 'ano' e 'total' para Integer
df_spark = df_spark.withColumn('ano', F.col('ano').cast(IntegerType()))
df_spark = df_spark.withColumn('total', F.col('total').cast(IntegerType()))

# 4. Imprimindo a contagem de linhas presentes no DataFrame
print("Total de linhas: ", df_spark.count())

# 5. Imprimindo a contagem de nomes, agrupando por ano e sexo
df_grouped = df_spark.groupBy('ano', 'sexo').count()
df_grouped_ordered = df_grouped.orderBy(F.col('ano').desc())  # Ordena por ano em ordem decrescente
df_grouped_ordered.show()

# 6. Nome feminino com mais registros e o ano
df_female = df_spark.filter(F.col('sexo') == 'F')
most_frequent_female = df_female.orderBy('total', ascending=False).first()
print(f"Nome feminino mais frequente: {most_frequent_female['nome']}, Ano: {most_frequent_female['ano']}")

# 7. Nome masculino com mais registros e o ano
df_male = df_spark.filter(F.col('sexo') == 'M')
most_frequent_male = df_male.orderBy('total', ascending=False).first()
print(f"Nome masculino mais frequente: {most_frequent_male['nome']}, Ano: {most_frequent_male['ano']}")

# 8. Total de registros (masculinos e femininos) para cada ano (10 primeiros crescente)
df_total_per_year_top_10 = df_spark.groupBy('ano').sum('total').orderBy(F.col('ano').asc()).limit(10)
df_total_per_year_top_10.show()

# 9. Gravando o DataFrame no S3 com valores de nome em maiúsculo
df_spark.write.partitionBy('sexo', 'ano').format('json').mode('overwrite').save(f"{target_path}")

# Finalizando o job
job.commit()
