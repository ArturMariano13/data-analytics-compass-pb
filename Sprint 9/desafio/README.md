# 🧩 Desafio da Sprint 9
Este diretório contém os arquivos necessários para a realização do desafio desta Sprint.

___

## 📝 Enunciado
O desafio da Sprint 9 é uma continuação do desafio iniciado na Sprint 6, sendo a quarta entrega do desafio final.

Esta etapa consiste na **modelagem dos dados e processamento da Camada *refined***. Nessa camada, os dados devem estar prontos para análise e extração de insights. A origem correspondente desses dados deve ser a camada Trusted, processada na Sprint 8.

Nesta Sprint devemos pensar em estruturar os dados seguindo os princípios de modelagem multidimensional, a fim de permitir consultas sobre diferentes perspectivas.

Será novamente utilizado o Apache Spark no processo, utilizando jobs cuja origem sejam dados da Trusted Zone, e o destino a camada Refined Zone. Os dados devem ser novamente persistidos no formato PARQUET, particionados, se necessário, de acordo com as necessidades definidas para a camada de visualização.

### Afazeres
- Criar tabelas no AWS Glue Data Catalog.
- Se necessário, criar *views* de acordo com a modelagem de dados solicitada.
- Criar camada *Refined*, tendo como origem os dados da camada *Trusted*.

### Entregáveis
- Arquivo markdown (este README) com evidências da realização do desafio + documentação de cada parte executada.
- Modelo de dados da camada Refined desenhado em ferramenta de modelagem.
- Código desenvolvido com devidos comentários.

--- 

## Resolução

### 1. Questões para análise

As questões para análise não foram alteradas, seguem as mesmas definidas na Sprint 7:

1. Quais foram os principais marcos que consolidaram Christopher Nolan como um dos diretores mais influentes do cinema mundial? 

2. Média de bilheteria de todos os filmes do ano 2000 e comparar com Memento (Amnésia) - primeiro filme de sucesso de Nolan.

3. Avaliação média de filmes de heróis em comparação à média dos filmes do Batman de Nolan.

4. Para colocar suas ideias em prática, Nolan precisa de orçamentos maiores do que outros filmes similares?


### 2. Modelagem dos dados

Por conseguinte, realizei a modelagem dos dados. Necessitei rever conceitos aprendidos e aplicados na Sprint 2 (modelagem dimensional - *star schema* e *snowflake*) para realizar essa tarefa.

Para realizar a modelagem, utilizei a ferramenta **brmodelo**, criando os seguintes fatos e dimensões:

![Imagem modelagem dos dados](../evidencias/2-modelagem.png)

- **dim_tempo:** contém a data de lançamento do filme, além dos campos ano, mês e dia, para facilitar análises posteriores.
- **dim_diretor:** contém o nome do diretor, no caso apenas filmes de Christopher Nolan conterão, os outros não foram coletados, pois não havia necessidade.
- **dim_genero:** contém o(s) gênero(s) dos filmes.
- **dim_titulo:** contém o título dos filmes.
- **fato_filme:** considerei o filme como o fato, contendo todas as informações numéricas do meu dataset: id, número de votos, nota média, orçamento e receita.

As cardinalidades são todas **1-n** devido à limitação da ferramenta brmodelo, porém entre o fato e a dimensão tempo deveria ser **1-1**, e a cardinalidade do lado da dimensão gênero deveria ser **1-n**, não 0-n. O restante está correto.


### 3. Criação do script local

Primeiramente optei por criar o script *on-premise* para posteriormente levar ao AWS Glue e executar em um job.

**3.1 - Download dos arquivos .parquet**

Busquei os arquivos .PARQUET processados na Sprint anterior e localizados na camada Trusted Zone para tê-los em minha máquina.

![Imagem download parquet](../evidencias/3.1-download-parquet.png)

**3.2 - Criação do script**

- **3.2.1**
    - Primeiro, criei um script que lia os arquivos .parquet e exibia os schemas, para entender todos os campos e como faria organizaria os dados para a modelagem efetuada.

![Imagem printSchemas](../evidencias/3.2-schemas.png)

- **3.2.2**
    - Posteriormente, realizei alguns testes de junção entre os dados do CSV (batch) e do TMDB, unindo pelo título do filme, haja vista que os ids eram diferentes.
    - Além disso, removi campos desnecessários, que não seriam efetivamente utilizados na análise final.

![Imagem dataframes unidos e limpos](../evidencias/3.3-dfLimpo.png) 








### 4. Job AWS Glue

**4.1 - Criação do job**

Primeiramente, criei o job no AWS Glue conforme solicitado no enunciado do exercício. A imagem abaixo comprova a criação do job.

![Imagem criação do job no AWS Glue](../evidencias/4.1-criacao-job.png)

**4.2 - Ajuste de parâmetros do job**

Agora, inseri os parâmetros com local de origem dos dados (camada Trusted) e onde eles serão salvos após execução do script (camada Refined).

![Imagem parâmetros job](../evidencias/4.2-parametros-job.png)

**4.3 - Criação do script do job**

Com o job criado e os parâmetros definidos, iniciei a construção do [script](script-glue.py) do job no Glue. Para isso, utilizei como base o script local desenvolvido anteriormente.

1. Imports necessários

![Imagem imports](../evidencias/4.3-script1.png)

- O código importa bibliotecas essenciais para executar um job no AWS Glue e manipular dados com PySpark.
- Bibliotecas essenciais para o uso do AWS Glue, o qual é utilizado para ETL (*Extract*, *Transform*, *Load*) na AWS.
- PySpark: usado para manipulação e processamento de dados distribuídos.
- Função `col` do PySpark para tratamento das colunas.


2. Configurações de ambiente (parâmetros, SparkContext e caminhos de arquivos)

![Imagem configurações de ambiente](../evidencias/4.3-script2.png)

- **Linha 11:** `getResolvedOptions` obtém os parâmetros necessários para rodar o job. Eles incluem o nome do job, o caminho de entrada `(S3_INPUT_PATH)`, e o caminho de saída `(S3_TARGET_PATH)`.
- **Linhas 14-18:** configurações necessárias para script no AWS Glue (fornecido pelo próprio serviço ao criar o job).
- **Linhas 20-21:** definição dos caminhos dos arquivos de entrada e saída, Trusted e Refined Zone respectivamente.
- **Linhas 23-24:** Leitura dos arquivos PARQUET para Spark DataFrames: `df_csv` com dados da ingestão batch (local) e `df_tmdb` com os dados da ingestão da API do TMDB.


3. Transformações nos DataFrames

![Imagem transformações DataFrames](../evidencias/4.3-script3.png)

- **Linha 27:** removi o id do `df_csv`, pois ambos os DataFrames possuíam id, porém esse id não era o mesmo, para que pudesse ser realizado um `join` por esse id. Por isso, escolhi remover o DataFrame do CSV.
- **Linha 28:** transformei a coluna `id` do DataFrame do TMDB em `long`, haja vista que ela era do tipo String.
- **Linha 31:** uni os DataFrames baseando-me pelo título do filme. Apesar de não ser a estratégia mais adequada, não havia outra informação (esperava que fosse o id) para realizar o `join`.
- **Linha 34:** removi alguns campos que julguei não serem mais necessários para a minha análise final.
- **Linha 35:** removi os duplicados pelo id do filme.
- **Linha 38:** printei o Schema do DataFrame para entender como havia ficado após essas transformações.


4. Ajuste no local de salvamento dos arquivos PARQUET

![Imagem salvamento PARQUET Movies](../evidencias/4.3-script4.png)

- Necessitei ajustar o local de salvamento dos arquivos PARQUET, inserindo mais um diretório: "Movies".

5. Tabela Fato `fato_filme`

![Imagem tabela fato_filme](../evidencias/4.3-script5.png)

- Para criar a tabela fato_filme, que conteria todos os campos numéricos e que se relacionaria com as demais dimensões, selecionei os campos: "id", "numeroVotos", "notaMedia", "orcamento" e "receita".
- Os dados são salvos no formato parquet no diretório /fato_filme dentro do caminho de destino.

6. Tabela Dimensional `dim_titulo`

![Imagem tabela dim_titulo](../evidencias/4.3-script6.png)

- A tabela armazena o id e o titulo do filme, e os dados são salvos no diretório /dim_titulo.

7. Tabela Dimensional `dim_tempo`

![Imagem tabela dim_tempo](../evidencias/4.3-script7.png)

- Colunas ano, mes, e dia são extraídas da coluna data_lancamento.
- Os dados são gravados no diretório /dim_tempo.

8. Tabela Dimensional dim_genero

![Imagem tabela dim_genero](../evidencias/4.3-script8.png)

- Seleciona as colunas id e genero e grava os dados no diretório /dim_genero.


9. Tabela Dimensional dim_diretor

![Imagem tabela dim_diretor](../evidencias/4.3-script9.png)

- Verifica se a coluna produtoras existe e contém valores não nulos. Se sim, cria-se uma coluna diretor com o valor fixo "Christopher Nolan" e grava esses dados no diretório /dim_diretor.

> Fiz essa validação, pois ao extrair os dados da API do TMDB, apenas os filmes cujas produtoras foram resgatadas pertencem à Christopher Nolan. Isso ocorreu, pois não busquei os diretores de todos os filmes, portanto a distinção entre ser de Christopher Nolan, ou não, ficou a critério de possuir ou não produtoras.

10. Finalização do job

![Imagem job commit](../evidencias/4.3-script91.png)

**4.4 - Job Runs**

Após desenvolver o script, executei o job. Fiz isso por diversas vezes, pois obtive erros no meio do caminho, os quais tiveram de ser solucionados resultando no script explicitado no item anterior.

![Imagem job runs](../evidencias/4.4-jobRuns.png)

**4.5 - Diretórios criados**

Os diretórios criados após a execução do job ficaram da seguinte maneira:

![Imagem diretórios pós execução do job](../evidencias/4.5-diretoriosExecucao.png)


### 5. Crawler

**5.1 - Criação**

Para criar as tabelas conforme requisitado, necessitei criar novamente um *crawler*, da mesma forma que na Sprint anterior. A imagem a seguir comprova a criação do Crawler, com a origem dos dados sendo a Refined Zone.

![Imagem criação Crawler](../evidencias/5.1-criandoCrawler.png)

**5.2 - Execução**

Após criar o *crawler*, executei-o para que ele criasse as tabelas baseado nos arquivos PARQUET gerados.

![Imagem execução crawler](../evidencias/5.2runCrawler.png)

**5.3 - Consulta das tabelas criadas**

Com isso, verifiquei se as tabelas haviam sido criadas corretamente no AWS Glue Data Catalog.

![Imagem tabelas criadas](../evidencias/5.3-tabelasCriadas.png)

**5.4 - Consulta no Amazon Athena**

Por fim, performei uma consulta no Amazon Athena para ver se as tabelas estavam preenchidas corretamente conforme o script desenvolvido.

![Imagem consulta Athena](../evidencias/5.4-consultaAthena.png)

___

### ↩️ [Retornar ao início](../../README.md)