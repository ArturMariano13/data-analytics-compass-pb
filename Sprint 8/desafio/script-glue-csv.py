import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as F
from pyspark.sql.types import IntegerType, FloatType
from datetime import datetime

# @params: [JOB_NAME, S3_INPUT_PATH, S3_TARGET_PATH]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

now = datetime.now()
DATA_ATUAL = now.strftime('%Y/%m/%d')

# Paths
source_file = args['S3_INPUT_PATH']  # Raw Zone
target_path = args['S3_TARGET_PATH']  # Trusted Zone

target_path = f'{target_path}/{DATA_ATUAL}/'

# 1. Ler os dados da Raw Zone
df_dynamic = glueContext.create_dynamic_frame.from_options(
    "s3",
    {
        "paths": [source_file]
    },
    "csv",
    {"withHeader": True, "separator": "|"}
)

# Convertendo para um DataFrame Spark
df_spark = df_dynamic.toDF()

# 2. Converter colunas para os tipos apropriados
df_spark = df_spark.withColumn("anoLancamento", F.col("anoLancamento").cast(IntegerType())) \
                   .withColumn("notaMedia", F.col("notaMedia").cast(FloatType())) \
                   .withColumn("numeroVotos", F.col("numeroVotos").cast(IntegerType()))

# 3. Selecionar colunas de interesse
df_selected = df_spark.select("id", "tituloPincipal", "tituloOriginal", "anoLancamento", 
                              "genero", "notaMedia", "numeroVotos")

# 4. Buscar todos os filmes em que Heath Ledger atuou
df_heath_ledger = df_spark.filter(F.col("nomeArtista").contains("Heath Ledger"))

# 5. Buscar filmes lançados entre 2000 e 2020
df_filmes_2000_2020 = df_selected.filter((F.col("anoLancamento") >= 2000) & 
                                         (F.col("anoLancamento") <= 2020))

# 6. Remover duplicados pelo id
df_deduplicated = df_filmes_2000_2020.dropDuplicates(["id"])

df_hlduplicated = df_heath_ledger.dropDuplicates(["id"])

# 7. Salvar o resultado no formato .parquet na Trusted Zone no S3
df_deduplicated.write \
    .mode('overwrite') \
    .format('parquet') \
    .save(f"{target_path}")

# 8. Também salvar os filmes do Heath Ledger, se necessário
df_heath_ledger.write \
    .mode('overwrite') \
    .format('parquet') \
    .save(f"{target_path}")

# 9. Finalizar o job
job.commit()
