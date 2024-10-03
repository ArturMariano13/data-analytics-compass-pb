# SPRINT 8 - Apache Spark

## Certificados
Para maiores informações sobre os certificados, siga o link: [certificados](certificados)

## Desafio
Para maiores informações sobre o desafio final, siga o link: [desafio](desafio)

## Evidências
Para maiores informações sobre as evidências, siga o link: [evidências](evidencias)

## Exercícios
Para maiores informações sobre os exercícios, siga o link: [exercícios](exercicios)

--- 

## Resumo dos Estudos

## Transformando dados em insights

- **Amazon Athena** - serverless, serviço de consultas interativas, facilita o acesso a dados no S3 (SQL).

- **AWS Glue** - integração de dados sem servidor.

- **Amazon QuickSight** - serviço de BI que utiliza Machine Learning (serverless).

### ETL com AWS Glue
- Pipelines ETL controlados por eventos.
- Catálogo unificado para localizar dados em vários armazenamentos de dados;
- Trabalhos ETL, sem necessidade de codificar.

### SQL padrão em S3 com Amazon Athena
- Apontar para dados no S3, definir Schema e fazer consultas.
- Baseado em Presto, executa SQL padrão.
- Pagamento por consulta.
- Desempenho interativo, rápido e serverless.

### Visualização dos dados com Amazon Quicksight
- Dimensione para dezenas de milhares de usuários.
- Paga por sessão, apenas quando usuários acessam.
- Acesso de insights mais profundos com *Machine Learning*.
- Incorporar painéis interativos BI em suas aplicações.

## Transformar e catalogar dados com AWS Glue

### AWS Glue
- Detecta automaticamente os dados e armazena o esquema.
- Dados pesquisáveis e disponíveis para ETL.
- Gera código personalizável.
- AWS Glue Studio.
- Sem servidor, flexível e baseado em padrões abertos.


## Consultar dados com o AWS Athena

- Serverless
- Padrão e aberto -> usa ANSI SQL para consultas com suporte para Parquet, CSV, JSOn, Avro, entre outros.
- Desempenho interativo rápido -> execução paralela para entregar a maioria dos resultados em segundos, sem a necessidade de gerenciamento de cluster.
- Custo efetivo -> pagar apenas pelas consultas executadas

## Visualizar dados com Amazon Qucksight
- Serevrless
- Análises incorporadas
- Insights baseados em Machine Learning

O QuickSight é alimentado pelo SPICE, um mecanismo de cálculo super rápido na memória que oferece desempenho e escala, independentemente de quantos usuários estejam ativos.



___