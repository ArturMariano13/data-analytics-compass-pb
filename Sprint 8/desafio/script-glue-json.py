import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as F
from pyspark.sql.types import DateType

# @params: [JOB_NAME, S3_INPUT_PATH, S3_TARGET_PATH]
# Obtém os argumentos necessários para o job
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

# Inicializa o contexto do Spark e o Glue
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Define os caminhos de entrada e saída
source_file = args['S3_INPUT_PATH']  # Diretório contendo os arquivos JSON na Raw Zone
target_path = args['S3_TARGET_PATH']  # Caminho da Trusted Zone para salvar os dados processados

# Lê os arquivos JSON do diretório especificado
dataFrame = spark.read \
    .option("multiLine", "false") \
    .json(source_file)

# Exibe o esquema do DataFrame
dataFrame.printSchema()

# Converte a coluna de data de lançamento para o formato de data
dataFrame = dataFrame.withColumn("data_lancamento", F.to_date(F.col("release_date"), "yyyy-MM-dd"))

# Captura o caminho do arquivo S3 para extração de data
dataFrame = dataFrame.withColumn("file_path", F.input_file_name())

# Extrai o ano, mês e dia do caminho do arquivo usando expressões regulares
dataFrame = dataFrame.withColumn("ano", F.regexp_extract(F.col("file_path"), r'.*/(\d{4})/(\d{2})/(\d{2})/', 1))
dataFrame = dataFrame.withColumn("mes", F.regexp_extract(F.col("file_path"), r'.*/(\d{4})/(\d{2})/(\d{2})/', 2))
dataFrame = dataFrame.withColumn("dia", F.regexp_extract(F.col("file_path"), r'.*/(\d{4})/(\d{2})/(\d{2})/', 3))

# Cria a coluna `data_criacao` combinando ano, mês e dia
dataFrame = dataFrame.withColumn("data_criacao", 
    F.concat_ws("-", F.col("ano"), F.col("mes"), F.col("dia")).cast(DateType())
)

# Corrige a coluna `production_companies` para concatenar os nomes das empresas
dataFrame = dataFrame.withColumn("production_companies", 
    F.concat_ws(", ", F.col("production_companies"))
)

# Seleciona as colunas de interesse para a Trusted Zone
trusted_data = dataFrame.select(
    dataFrame.id.alias("id"),
    dataFrame.title.alias("titulo"),
    dataFrame.release_date.alias("data_lancamento"),
    dataFrame.popularity.alias("popularidade"),
    dataFrame.budget.alias("orcamento"),
    dataFrame.revenue.alias("receita"),
    dataFrame.production_companies.alias("produtoras"),
    dataFrame.data_criacao.alias("data_criacao")
)

# Exibe os dados selecionados
trusted_data.show(truncate=False)

# Salva os dados em formato Parquet, particionando pela data de criação
trusted_data.write \
    .partitionBy("data_criacao") \
    .mode("overwrite") \
    .parquet(target_path)

# Finaliza o job
job.commit()
