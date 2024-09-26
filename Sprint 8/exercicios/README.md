# Exercícios da Sprint 8
Este diretório contém os exercícios da Sprint 8. 

## 1 - Exercícios Spark Batch
## 1.1 - Geração e massa de dados

### Etapa 1 - Lista aleatória de números inteiros

**RESOLUÇÃO** 

1. Importação da biblioteca `random`

![Imagem biblioteca random Python](../evidencias/ev_exercicios/1-ESB1.1-librandom.png)

2. Geração da lista aleatoriamente (250 valores), com o método `random.randint(min, max)` - selecionei de 1 a 10000.

![Imagem geração números aleatórios](../evidencias/ev_exercicios/1-ESB1.2-geracaolista.png)

3. Aplicação do método `reverse()`

![Imagem método reverse](../evidencias/ev_exercicios/1-ESB1.3-metodoreverse.png)

4. Mostrar resultado

![Imagem print](../evidencias/ev_exercicios/1-ESB1.4-print.png)


**EVIDÊNCIA EXECUÇÃO**

Executei duas vezes para mostrar a pseudo-aleatoriedade para geração dos valores.

![Imagem evidência execução](../evidencias/ev_exercicios/1-ESB1.5-execucao.png)

- [**SCRIPT FINAL**](1-spark-batch/etapa1.py)


### Etapa 2 - Lista de animais em arquivo CSV 

**RESOLUÇÃO**

1. Criação da lista com nomes de animais diferentes (20)

![Imagem criação da lista Python](../evidencias/ev_exercicios/1-ESB2.1-criacaolista.png)

2. Ordenação da lista com método `sort()`

![Imagem ordenação da lista Python](../evidencias/ev_exercicios/1-ESB2.2-ordenacao.png)

3. Print animais com *list comprehension*

![Imagem print](../evidencias/ev_exercicios/1-ESB2.3-printlistcomprehension.png)

4. Escrita em arquivo CSV

![Imagem escrita CSV](../evidencias/ev_exercicios/1-ESB2.4-escritaarquivocsv.png)


**EXECUÇÃO**

1. Console

![Imagem print console](../evidencias/ev_exercicios/1-ESB2.5-execucao.png)

2. Arquivo CSV - [ver arquivo](1-spark-batch/animais.csv)

![Imagem CSV](../evidencias/ev_exercicios/1-ESB2.6-arquivocsv.png)


- [**SCRIPT FINAL**](1-spark-batch/etapa2.py)
- [**ARQUIVO .CSV**](1-spark-batch/animais.csv)


### Etapa 3 - Gerar dataset de nomes de pessoas

**RESOLUÇÃO**

1. Instalação da biblioteca `names`

![Imagem instalação biblioteca names](../evidencias/ev_exercicios/1-ESB3.1-libnames.png)

2. Importação das bibliotecas necessárias (`random`, `time`, `os`, `names`)

![Imagem import bibliotecas](../evidencias/ev_exercicios/1-ESB3.2-importlibs.png)

3. Definição dos parâmetros para a geração do dataset: quantidade de nomes aleatórios e quantidade de nomes únicos (trecho de código fornecido pelo enunciado do exercício)

![Imagem definição de parâmetros](../evidencias/ev_exercicios/1-ESB3.3-inicializacaovariaveis.png)

4. Geração de nomes aleatórios (trecho de código fornecido pelo enunciado do exercício)

![Imagem código para geração de nomes aleatórios](../evidencias/ev_exercicios/1-ESB3.4-geracaonomesaleatorios.png)

5. Geração de arquivo texto com todos os nomes

![Imagem criação de arquivo texto](../evidencias/ev_exercicios/1-ESB3.5-geracaoarquivo.png)

6. Visualização do conteúdo do arquivo texto

![Imagem arquivo texto](../evidencias/ev_exercicios/1-ESB3.7-execucao2.png)


**EXECUÇÃO**

![Imagem execução script](../evidencias/ev_exercicios/1-ESB3.6-execucao1.png)

- [**SCRIPT FINAL**](1-spark-batch/etapa3.py)
- [**ARQUIVO TEXTO**](1-spark-batch/nomes_aleatorios.txt)

---

## 1.2 - Apache Spark

### Etapa 1 - Preparação do ambiente

1. Import de bibliotecas

![Imagem import bibliotecas](../evidencias/ev_exercicios/2-ESB1.1-importlibs.png)

2. Definição da SparkSession (fornecido pelo enunciado do exercício)

![Imagem SparkSession](../evidencias/ev_exercicios/2-ESB1.2-sparksession.png)

3. Leitura do arquivo em dataframe (df_nomes) e exibição

![Imagem leitura e exibição dados](../evidencias/ev_exercicios/2-ESB1.3-leituraexibicao.png)

4. Evidência da execução

![Imagem evidência execução](../evidencias/ev_exercicios/2-ESB1.4-execucao.png)

- [**SCRIPT 1**](2-apache-spark/etapa1.py)

### Etapa 2 - Renomear coluna para Nomes, imprimir esquema e mostrar 10 linhas do dataframe

1. Biblioteca pyspark e leitura do arquivo (igual à etapa anterior)

![Imagem bibliotecas e leitura arquivo](../evidencias/ev_exercicios/2-ESB2.1-libsleitura.png)

2. `printSchema()`

![Imagem printSchema código](../evidencias/ev_exercicios/2-ESB2.2-printschema.png)

![Imagem printSchema execução](../evidencias/ev_exercicios/2-ESB2.3-printschema-execucao.png)

3. Renomeação da coluna
- Ao executar `printSchema`, percebi que o nome da coluna adotado pelo Spark foi **_c0**. Por isso, no método `withColumnRenamed()` esse foi o primeiro parâmetro (coluna atual).

![Imagem renomeação coluna](../evidencias/ev_exercicios/2-ESB2.4-renomeacao.png)

3. Alteração do schema
- Com isso, executei novamente o método `printSchema()` para garantir a alteração do nome da coluna.
- O resultado foi:

![Imagem do schema após renomeação](../evidencias/ev_exercicios/2-ESB2.5-schemaalterado.png)

4. Mostrar  10 linhas do dataframe

![Imagem código para mostrar 10 primeiras linhas do dataframe](../evidencias/ev_exercicios/2-ESB2.6-dezlinhas.png)

![Imagem 10 primeiras linhas do dataframe](../evidencias/ev_exercicios/2-ESB2.7-dezlinhas-execucao.png)

5. Evidência da execução total

![Imagem execução script inteiro](../evidencias/ev_exercicios/2-ESB2.8-execucaototal.png)

- [**SCRIPT 2**](2-apache-spark/etapa2.py)

### Etapa 3 - Inclusão da coluna "Escolaridade"

1. O código das etapas anteriores permanece, conforme as figuras abaixo:

![Imagem código etapas anteriores](../evidencias/ev_exercicios/2-ESB3.1-libs.png)

![Imagem código etapas anteriores 2](../evidencias/ev_exercicios/2-ESB3.2-sparksession-etapa2.png)

2. Primeiramente, criei o método `escolher_escolaridade()`, o qual retorna uma opção aleatória entre "Fundamental", "Médio" e "Superior", utilizando a lib random.

3. Além disso, criei uma UDF (*User Defined Function*), a qual consiste em uma função do PySpark que converte uma função do Python simples em uma função que pode ser aplicada sobre colunas de um DataFrame.

4. Dessa forma, com o `withColumn()`, criei a nova coluna "Escolaridade". 

5. Por fim, são mostradas as 10 primeiras linhas do DataFrame.

![Imagem funcionalidade etapa 3](../evidencias/ev_exercicios/2-ESB3.3-etapa3.png)

6. **Execução**

![Imagem execução etapa 3](../evidencias/ev_exercicios/2-ESB3.4-execucao.png)

[**SCRIPT 3**](2-apache-spark/etapa3.py)

### Etapa 4 - Inclusão da coluna "País"

A inclusão da coluna país correu de modo similar à etapa anterior:

1. Manteve-se as etapas anteriores no código desta etapa:

![Imagem etapas anteriores](../evidencias/ev_exercicios/2-ESB4.1-etapas123.png)

2. Criou-se uma função `escolher_pais()`, a qual foi utilizada como `udf()`, retornando uma escolha aleatória entre os 13 paízes da América do Sul.

![Imagem código etapa 4](../evidencias/ev_exercicios/2-ESB4.2-resolucao.png)

3. O restante ficou exatamente igual à etapa anterior.

4. **Execução**

![Imagem execução etapa 4](../evidencias/ev_exercicios/2-ESB4.3-execucao.png)

### Etapa 5 - Inclusão da coluna "AnoNascimento"

A inclusão da coluna AnoNascimento ocorreu basicamente da mesma forma que as duas etapas anteriores, porém com a diferença de ser valores inteiros.

Com isso, necessitou-se adicionar o módulo IntegerType. 

![Imagem código](../evidencias/ev_exercicios/2-ESB5.1-imports.png)

- **Execução**

![Imagem execução](../evidencias/ev_exercicios/2-ESB5.2-execucao.png)


### Etapa 6 - Pessoas que nasceram neste século

A etapa 6, por outro lado, solicitou uma filtragem e a utilização do método `select` do Spark, selecionando apenas pessoas que nasceram no século XXI.

Para isso, utilizei o método `.filter()` filtrando apenas pelos anos de nascimento a partir do ano 2000, além de selecionar nomes e AnoNascimento.

![Imagem código desenvolvido](../evidencias/ev_exercicios/2-ESB6.1-codigo.png)

- **Execução**

![Imagem execução](../evidencias/ev_exercicios/2-ESB6.2-execucao.png)


### Etapa 7 - Utilizar SparkSQL no mesmo caso da etapa 6

A etapa 7 visa realizar a mesma atividade da etapa anterior, porém com a utilização do Spark SQL.

![Imagem código](../evidencias/ev_exercicios/2-ESB7.1-codigo.png)

- **Execução**

![Imagem execução](../evidencias/ev_exercicios/2-ESB7.2-execucao.png)


### Etapa 8 - Pessoas da geração *Millenials* (select Dataframe)

A etapa 8 é bastante similar à 6ª etapa, porém necessita incluir duas validações: maior ou igual a 1980 e menor ou igual a 1994.

![Imagem código](../evidencias/ev_exercicios/2-ESB8.1-codigo.png)

- **Execução**

![Imagem execução](../evidencias/ev_exercicios/2-ESB8.2-execucao.png)

### Etapa 9 - SparkSQL na etapa 8

A etapa 9 é bastante similar à etapa 7, basta solucionar o problema da etapa 8 com a utilização de Spark SQL.

![Imagem código](../evidencias/ev_exercicios/2-ESB9.1-codigo.png)

- **Execução**

![Imagem execução](../evidencias/ev_exercicios/2-ESB9.2-execucao.png)

### Etapa 10 - SparkSQL para dividir em gerações e países

A etapa 10 pediu uma query que contasse todos os registros de gerações por país, ordenando por país e por geração.

Dessa forma, primeiramente defini uma *string* chamada *query* e realizei a query da mesma forma que nas etapa 9 e 7.

![Imagem código](../evidencias/ev_exercicios/2-ESB10.1-codigo.png)

- **Execução**

![Imagem execução](../evidencias/ev_exercicios/2-ESB10.2-execucao.png)


Dessa forma, finaliza-se os exercícios de Spark. Ao final produzi um script final com todas as operações, uma a uma:

[**SCRIPT FINAL**](2-apache-spark/script-final.py)

---

## 2 - Exercícios TMDB

### Etapa 1 - Criação da conta TMDB

A conta de desenvolvedor no TMDB já havia sido criada na Sprint anterior para realizar o desafio. Por isso, apenas insiro um print comprovando a criação de minha conta:

![Imagem conta TMDB](../evidencias/ev_exercicios/3.1-conta-tmdb.png)

### Etapa 2 - Teste de credenciais e biblioteca

O código deste exercício foi fornecido pelo enunciado, portanto apenas o copiei e adaptei para utilizar a minha API_KEY (que inseri em outro arquivo - `config.py`).

![Imagem código](../evidencias/ev_exercicios/3.2-codigo.png)

**Execução**

![Imagem execução](../evidencias/ev_exercicios/3.3-execucao.png)


[**SCRIPT FINAL**](3-tmdb/etapa2.py)














___

### ↩️ [Retornar ao início](../../README.md)