# 🧩 Desafio da Sprint 8
Este diretório contém os arquivos necessários para a realização do desafio desta Sprint.

___

## 📝 Enunciado
O desafio da Sprint 8 é uma continuação do desafio iniciado na Sprint 6, sendo a terceira entrega do desafio final.

Esta etapa consiste no **processamento da camada *trusted***, com essa possuindo os dados limpos e confiáveis. Consiste na integração das diversas fontes de origem (dados que estão na camada Raw).

Será utilizado Apache Spark através do serviço AWS Glue, integrando dados existentes na camada *Raw Zone* para a *Trusted Zone*. Todos os dados da *Trusted Zone* devem possuir o mesmo formato de armazenamento e poder ser analisados no AWS Athena por meio de SQL.

Os dados serão persistidos no formato PARQUET, particionados por data de criação do arquivo no momento da ingestão do dado da TMDB. A exceção fica para os dados oriundos do processamento *batch* (CSV), que não precisam ser particionados.

Iremos separar o processamento em dois jobs:
1. Processamento dos arquivos CSV
2. Processamento dos dados oriundos da API TMDB.

> OBS.: Não utilizar notebooks do Glue.


## Resolução

### 1. Criação e permissões de usuário IAM

Na Sprint anterior, no exercício Lab AWS Glue, tivemos de criar um usuário IAM para fornecer permissões e realizar as operações necessárias. No entanto, ao encerrar a Sprint, excluí todos os recursos criados por mim durante a Sprint, necessitando agora criar outro usuário IAM.

Sendo assim, criei o usuário e configurei a *Role* para o Glue.

![Imagem criação IAM user](../evidencias/ev_desafio/1-usuarioIAM.png)

![Imagem configuração IAM Role](../evidencias/ev_desafio/1.1-configRole1.png)

![Imagem configuração IAM Role 2](../evidencias/ev_desafio/1.2-configRole2.png)

### 2. Configurações de permissões no AWS Lake Formation

**2.1. Criação de *Database***

![Imagem criação database](../evidencias/ev_desafio/2-criacaoDatabase.png)

**2.2. Adição do usuário IAM como Administrador do *data lake***

![Imagem configuração Administrador data lake](../evidencias/ev_desafio/2.1-confLakeFormation.png)

**2.3. Alteração de permissões do *Database***

![Imagem alteração de permissões do database](../evidencias/ev_desafio/2.2-grantPermissions.png)

### 3. Criação dos jobs

Cada um dos jobs fica responsável por dados ingeridos de maneira distinta:

- **job-batch-data**: dados CSV processados em lote (Sprint 6).

![Imagem criação job dados ingestão Batch](../evidencias/ev_desafio/3-criacaoJobBatch.png)

- **job-tmdb-data**: dados JSON ingeridos da API do TMDB (Sprint 7).

![Imagem criação job dados API TMDB](../evidencias/ev_desafio/3.1-criacaoJobTMDB.png)


![Imagem jobs AWS Glue](../evidencias/ev_desafio/3.2-jobsCriados.png)

Por conseguinte, foi necessário alterar os parâmetros com os locais de busca dos arquivos Raw e de salvamento dos arquivos na camada Trusted.

![Imagem alteração de parâmetros para Script](../evidencias/ev_desafio/3.3-alteracaoParametros.png)

### 4. Desenvolvimento dos Scripts

### 4.1. Script dados *Batch*

1. **Importações e dependências**

![Imagem bibliotecas script](../evidencias/ev_desafio/4.1.1-bibliotecas.png)

- `sys`: para acessar argumentos de linha de comando.
- `awsglue.transforms, awsglue.utils, awsglue.context, awsglue.job`: bibliotecas da AWS Glue para trabalhar com jobs, criar contextos e transformar dados.
- `pyspark.sql.functions` e `pyspark.sql.types`: funções e tipos de dados do PySpark para manipulação e conversão de colunas no DataFrame.
- `datetime`: utilizado para gerar o timestamp da execução.


2. **Definição dos parâmetros do job**

![Imagem parâmetros do job](../evidencias/ev_desafio/4.1.2-parametros.png)

Aqui são obtidos os argumentos passados ao job (nome do job, caminho de entrada e saída no S3).


3. **Criação do contexto do Spark e inicialização do job**

![Imagem criação de contexto do Spark](../evidencias/ev_desafio/4.1.3-contextoSpark.png)

- `SparkContext`: inicializa o contexto do Spark.
- `GlueContext`: cria um contexto do Glue para utilizar suas funcionalidades no Spark.
- `spark_session`: cria uma sessão Spark para manipular DataFrames.
- `job.init`: inicializa o job Glue usando o nome passado via parâmetro.


4. **Definição de variáveis e preparação de caminhos**

![Imagem definição de variáveis e preparação de caminhos](../evidencias/ev_desafio/4.1.4-variaveisCaminhos.png)

- `now`: armazena a data e hora atuais.
- `DATA_ATUAL`: formata a data para ser utilizada nos caminhos de saída.
- `source_file`: caminho do arquivo de entrada na "Raw Zone".
- `target_path`: caminho do arquivo de saída na "Trusted Zone", que inclui a data no caminho.


5. **Leitura dos dados da Raw Zone**

![Imagem leitura de dados da Raw Zone](../evidencias/ev_desafio/4.1.5-leituraDadosRawZone.png)

- `create_dynamic_frame`: lê o arquivo CSV diretamente do S3.
- `withHeader`: indica que o arquivo CSV contém um cabeçalho.
- `separator`: define o separador de colunas (neste caso, é **|**).


6. **Conversão para DataFrame Spark**

Converti o *DynamicFrame* (estrutura nativa do AWS Glue) para um DataFrame do Spark para facilitar as transformações.

![Imagem conversão para DataFrame Spark](../evidencias/ev_desafio/4.1.6-conversaoDataFrameSpark.png)


7. **Conversão de colunas para os tipos apropriados**

![Imagem conversão de colunas](../evidencias/ev_desafio/4.1.7-conversaoTiposDados.png)

- anoLancamento: para *IntegerType*.
- notaMedia: para *FloatType*.
- numeroVotos: para *IntegerType*.


8. **Seleção das colunas desejadas**

Selecionei apenas as colunas relevantes do DataFrame original: ID, títulos (principal e original), ano de lançamento, gênero, nota média e número de votos.

![Imagem seleção de colunas desejadas](../evidencias/ev_desafio/4.1.8-selecaoDados.png)


9. **Filtragem de filmes**

- Filtragem dos filmes que foram lançados entre os anos de 2000 e 2020.

![Imagem filmes entre 2000 e 2020](../evidencias/ev_desafio/4.1.9-filmesSeculo.png)

- Filtragem dos filmes em que Heath Ledger atuou.

![Imagem filmes de Heath Ledger](../evidencias/ev_desafio/4.1.10-heathLedger.png)


10. **Remoção de duplicados pelo id**

![Imagem remoção de duplicados por id](../evidencias/ev_desafio/4.1.11-remocaoDuplicados.png)


11. **Salvamento do resultado no S3 em formato Parquet**

![Imagem salvamento em Parquet no S3](../evidencias/ev_desafio/4.1.12-salvamentoParquet.png)


12. **Finalização do job**

![Imagem finalização do job](../evidencias/ev_desafio/4.1.13-finalizacaoJob.png)


13. **Execução do Script**

- Job runs:

![Imagem execução script dados Batch - job runs](../evidencias/ev_desafio/4.1.14-execucaoScript.png)

- Estrutura de diretórios:

![Imagem execução script dados Batch - diretórios](../evidencias/ev_desafio/4.1.15-execucaoDiretorios.png)


### 4.2. Script dados API TMDB

1. **Bibliotecas necessárias**

![Imagem importações de bibliotecas](../evidencias/ev_desafio/4.2.1-bibliotecas.png)


2. **Parâmetros**

![Imagem parâmetros do job](../evidencias/ev_desafio/4.2.2-parametros.png)


3. **Inicialização do contexto Glue**

![Imagem contexto Glue](../evidencias/ev_desafio/4.2.3-contextoGlue.png)


4. **Definição de Caminhos**

![Imagem definição dos caminhos](../evidencias/ev_desafio/4.2.4-caminhos.png)


5. **Leitura de arquivos JSON**

Para realizar a leitura dos arquivos JSON utilizei o DataFrame do Spark diretamente, sem utilizar o DynamicFrame (nativo do Glue). Isso, pois inicialmente tentei utilizar a mesma estratégia do passo anterior, para ler o arquivo CSV, mas não obtive sucesso. Modificando isso, consegui realizar corretamente.

![Imagem leitura dos arquivos JSON](../evidencias/ev_desafio/4.2.5-leituraArquivosJSON.png)


6. **Conversão de Colunas**

![Imagem conversão de coluna release_date](../evidencias/ev_desafio/4.2.6-conversaoReleaseDate.png)

Converte a coluna *release_date* para o formato de data, renomeando-a para *data_lancamento*.


7. **Captura do Caminho do Arquivo S3**

![Imagem adição de nome do arquivo do S3](../evidencias/ev_desafio/4.2.7-capturaNomeArquivo.png)

Adiciona uma nova coluna *file_path* que contém o caminho do arquivo S3 de onde os dados foram lidos.


8. **Extração de Data a Partir do Caminho do Arquivo**

![Imagem extração ano, mês e dia](../evidencias/ev_desafio/4.2.8-extracaoAnoMesDia.png)

Utiliza expressões regulares para extrair o ano, mês e dia do caminho do arquivo, armazenando-os em novas colunas ano, mes e dia.


9. **Criação da Coluna de Data de Criação**

![Imagem criação de coluna data de criação](../evidencias/ev_desafio/4.2.9-criacaoColunaDataCriacao.png)

Combina as colunas de ano, mês e dia em uma nova coluna chamada `data_criacao`, convertendo-a para o tipo de dado `DateType`.


10. **Correção da Coluna de Empresas de Produção**

![Imagem correção coluna production_companies](../evidencias/ev_desafio/4.2.10-correcaoProductionCompanies.png)

Concatena os nomes das empresas de produção em uma única string, separando-os por vírgulas.


11. **Seleção das Colunas de Interesse**

![Imagem seleção de campos desejados](../evidencias/ev_desafio/4.2.11-selecaoCampos.png)


12. **Salvamento dos Dados em Formato Parquet**

![Imagem salvamento dos dados em Parquet](../evidencias/ev_desafio/4.2.12-salvamentoDF.png)


13. **Finalização do Job**

![Imagem finalização do Job](../evidencias/ev_desafio/4.2.13-finalizacaoJob.png)


14. **Execução script**

- Job runs:

![Imagem execução script dados TMDB - job runs](../evidencias/ev_desafio/4.2.14-execucaoScript.png)

**Execução do Script**
- Estrutura de diretórios: 

![Imagem execução script dados TMDB - diretórios](../evidencias/ev_desafio/4.2.15-execucaoDiretorios.png)


### 5. Criação de Crawler

Depois, necessitamos criar um Crawler para criar uma tabela a partir dos dados do S3 automaticamente.

![Imagem criação Crawlers](../evidencias/ev_desafio/5-crawlersCriados.png)

Sendo assim, os crawlers criados geraram as tabelas abaixo:

![Imagem tabelas criadas](../evidencias/ev_desafio/5.1-tabelasCriadas.png)

### 6. Consultando dados com Athena

**6.1. Consulta na tabela dos dados CSV**

![Imagem select tudo](../evidencias/ev_desafio/6.1-selectBatch.png)

![Imagem resultados select](../evidencias/ev_desafio/6.1.1-selectBatchResultado.png)


**6.2. Consulta na tabela dos dados JSON (TMDB)**

Primeiramente, ao tentar realizar *selects* na tabela "parquet", criada com os dados provenientes do TMDB, obtive uma tabela sem registros (vazia). Para isso, necessitei dar o seguinte comando: 

![Imagem comando correção select](../evidencias/ev_desafio/6.2.3-comandoParticao.png)

O comando `MSCK REPAIR TABLE nometabela` é utilizado no contexto do Apache Hive e do Amazon Athena, que são ferramentas de processamento de dados que trabalham com grandes volumes de informações armazenadas em sistemas distribuídos, como o Amazon S3. A função desse comando é manter a integridade da tabela que está sendo utilizada para consultar dados particionados.

Nesse caso, como a tabela possui dados particionados, necessitei executar esse comando.

Após isso realizado, pude realizar os comandos de seleção na tabela:

![Imagem select tudo TMDB](../evidencias/ev_desafio/6.2-selectTMDB.png)

![Imagem resultados select](../evidencias/ev_desafio/6.2.1-selectTMDBResultados.png)

![Imagem resultados select 2](../evidencias/ev_desafio/6.2.2-selectTMDBResultados.png)

___

### ↩️ [Retornar ao início](../../README.md)