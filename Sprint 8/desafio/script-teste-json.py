import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as F
from pyspark.sql.types import IntegerType, FloatType, DateType, DoubleType
import re

# @params: [JOB_NAME, S3_INPUT_PATH, S3_TARGET_PATH]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Paths
source_file = args['S3_INPUT_PATH']  # Raw Zone - Diretório contendo os arquivos JSON
target_path = args['S3_TARGET_PATH']  # Trusted Zone

"""
try:
    # 1. Ler os dados JSON da Raw Zone
    print(f"Tentando ler os dados JSON de: {source_file}")
    df_dynamic = glueContext.create_dynamic_frame.from_options(
        connection_type = "s3", 
        connection_options = {
            "paths": [source_file]
        },
        format = "json"
    )
    print("Leitura bem-sucedida.")
    
except Exception as e:
    print(f"Erro ao ler os dados JSON: {e}")
    sys.exit(1)  # Encerra o job em caso de erro

try:
    # Convertendo para um DataFrame Spark
    df_spark = df_dynamic.toDF()
    print("Conversão para DataFrame Spark bem-sucedida.")

    # Exibindo o esquema do DataFrame
    print("Esquema do DataFrame:")
    df_spark.printSchema()

    # Exibindo os dados
    print("Dados do DataFrame:")
    df_spark.show(truncate=False)

except Exception as e:
    print(f"Erro ao converter para DataFrame Spark ou ao exibir dados: {e}")
    sys.exit(1)  # Encerra o job em caso de erro

df_spark = df_spark.withColumn("data_lancamento", F.col("release_date").cast(DateType())) \
                   .withColumn("nota_media", F.col("vote_average").cast(FloatType())) \
                   .withColumn("id", F.col("id").cast(IntegerType())) \
                   .withColumn("receita", F.col("revenue").cast(DoubleType())) \
                   .withColumn("orcamento", F.col("budget").cast(DoubleType())) \
                   .withColumnRenamed("title", "titulo") \
                   .withColumnRenamed("popularity", "popularidade") \
                   .withColumn("data", F.lit(data_completa))
    
# 6. Remover duplicados pelo id
df_deduplicated = df_spark.dropDuplicates(["id"])

# 7. Salvar o DataFrame em formato Parquet, particionado por data
df_deduplicated.write.mode("overwrite") \
    .partitionBy("data") \
    .parquet(parquet_output)
"""

dataFrame = spark.read \
     .option("multiLine", "false") \
     .json(source_file)

dataFrame.printSchema()

dataFrame = dataFrame.withColumn("data_lancamento", F.col("release_date").cast(DateType()))

# 4. Extração da data de criação a partir do caminho do arquivo S3
# Usando a função input_file_name() para capturar o caminho do arquivo
dataFrame = dataFrame.withColumn("file_path", F.input_file_name())

# Extraindo ano, mês e dia do caminho usando regexp_extract()
# Exemplo de caminho: s3://bucket/Raw/TMDB/JSON/2024/09/23/arquivo.json
dataFrame = dataFrame.withColumn("ano", F.regexp_extract(F.col("file_path"), r'.*/(\d{4})/(\d{2})/(\d{2})/', 1))
dataFrame = dataFrame.withColumn("mes", F.regexp_extract(F.col("file_path"), r'.*/(\d{4})/(\d{2})/(\d{2})/', 2))
dataFrame = dataFrame.withColumn("dia", F.regexp_extract(F.col("file_path"), r'.*/(\d{4})/(\d{2})/(\d{2})/', 3))

# Criando a coluna `data_criacao` combinando ano, mês e dia
dataFrame = dataFrame.withColumn("data_criacao", 
    F.concat_ws("-", F.col("ano"), F.col("mes"), F.col("dia")).cast(DateType())
)

# 5. Verificar se a coluna de data de criação foi criada corretamente
dataFrame.select("file_path", "data_criacao").show(truncate=False)

# 6. Salvar os dados em formato Parquet, particionando pela data de criação (data_criacao)
dataFrame.write \
    .partitionBy("data_criacao") \
    .mode("overwrite") \
    .parquet(target_path)

# 7. Finalizar o job
job.commit()
