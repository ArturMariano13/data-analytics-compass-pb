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


### 4.2. Script dados API TMDB


### 5. Criação de Crawler

Depois, necessitamos criar um Crawler para criar uma tabela a partir dos dados do S3 automaticamente.

![Imagem criação Crawler 1](../evidencias/ev_desafio/5-criandoCrawler.png)

![Imagem criação Crawler 2 - definindo dataSource](../evidencias/ev_desafio/5.1-crawlerDataSource.png)

![Imagem criação Crawler 3](../evidencias/ev_desafio/5.2-criandoCrawlerFinal.png)

### 6. Evidências execução



___

### ↩️ [Retornar ao início](../../README.md)