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

- [**SCRIPT FINAL**](2-apache-spark/etapa1.py)

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

- [**SCRIPT FINAL**](2-apache-spark/etapa2.py)

### Etapa 3 - 















___

### ↩️ [Retornar ao início](../../README.md)