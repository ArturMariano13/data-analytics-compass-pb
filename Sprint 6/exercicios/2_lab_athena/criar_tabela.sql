CREATE EXTERNAL TABLE IF NOT EXISTS meubanco.nomes (
  Nome STRING,
  Sexo CHAR(1),
  Total INT,
  Ano INT
  
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES (
 'serialization.format' = ',',
 'field.delim' = ','
)
LOCATION 's3://bucket-ex1-sprint6/dados';