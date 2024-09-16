# Exercícios da Sprint 7
Este diretório contém os exercícios da Sprint 7. 

São dois (2) exercícios: Laboratório de AWS Glue e outro envolvendo a criação de um contador de palavras com Apache Spark.

## 1. Apache Spark - Contador de Palavras

### Etapa 1 - *Pull* da imagem docker

O pull da imagem sugerida no enunciado do exercício pode ser realizada pelo seguinte comando:

```bash
docker pull jupyter/all-spark-notebook
```

![Imagem pull imagem](../evidencias/1-apache-spark-pull-image.png)

![Imagem imagem local](../evidencias/1.1-apache-spark-image-ls.png)


### Etapa 2 - Criação do container a partir da imagem
A criação do container deve ter `-it` como argumento, para rodar de modo interativo, além de mapear a porta 8888 exposta pelo serviço para a máquina local.

```bash
docker run --name <nome-container> -it -p 8888:8888 jupyter/all-spark-notebook
```

![Imagem execução container](../evidencias/2-apache-spark-docker-run.png)

![Imagem comprovação execução](../evidencias/2.1-apache-spark-teste.png)

### Etapa 3 - Execução no terminal
1. **Download do arquivo 'README.md'**

Primeiramente necessita-se fazer o download do arquivo README do meu GitHub. Para isso, primeiramente deve-se executar o container abrindo o terminal bin/bash dele.

`docker exec -it <nome-container> /bin/bash`

Com isso, no terminal do container, pode-se fazer o download do arquivo por meio do comando `wget`.

```bash
wget <url-README>
```

Com isso, o arquivo será baixado para o diretório atual. Para facilitar o manuseio posterior, deve-se renomeá-lo, pois ele vem com um nome gerado aleatoriamente.

```bash
mv <nome-arquivo> <README.md>
```

![Imagem download README](../evidencias/3-apache-spark-wget.png)

Dessa forma, poderá ser acessado pelo **pyspark** na próxima etapa.

### Etapa 4 - Contagem de Palavras com PySpark

Nesta etapa, necessitava-se utilizar o PySpark para contar o número total de palavras em um arquivo de texto. A seguir, há o detalhamento do processo realizado.

1. **Inicialização do PySpark Shell**
    
A inicialização do shell do PySpark no contêiner Spark foi realizado com o seguinte comando:

```bash
   docker exec -it container-spark pyspark
```

2. **Leitura do Arquivo**

```python
arquivo = spark.read.text("README.md")
```
Isso cria um DataFrame arquivo onde cada linha representa uma linha do arquivo.

3. **Limpeza e Preparação do Texto**

Para garantir que apenas palavras efetivas fossem consideradas, o texto foi limpo de tags HTML e caracteres especiais. Utilizou-se a função `regexp_replace` para realizar a limpeza:

```python
from pyspark.sql.functions import col, regexp_replace

# Remove tags HTML utilizadas
texto_limpo = arquivo.select(regexp_replace(col("value"), "<[^>]*>", "").alias("value"))

# Remove caracteres não alfanuméricos e múltiplos espaços
texto_limpo = texto_limpo.select(
    regexp_replace(col("value"), "[^a-zA-Z0-9\\s]", "").alias("value")
)

```

4. **Divisão do Texto em Palavras**

O texto limpo foi dividido em palavras. Utilizou-se a função split para separar o texto por espaços e a função explode para transformar cada linha em várias linhas, cada uma contendo uma palavra:

```python
from pyspark.sql.functions import split, explode, lower

palavras = texto_limpo.select(
    explode(
        split(lower(col("value")), "\\s+")
    ).alias("palavra")
)
```

5. **Filtragem de Palavras Vazias**

As palavras vazias foram filtradas para garantir uma contagem precisa:

```python
palavras_filtradas = palavras.filter(col("palavra") != "")
```

6. **Contagem das Ocorrências de Palavras**

A contagem das ocorrências de cada palavra foi realizada, agrupando as palavras e contando suas aparições:

```python
contagem_palavras = palavras_filtradas.groupBy("palavra").count()
```

7. **Ordenação e Exibição das Palavras Mais Frequentes**

As palavras foram ordenadas pela contagem em ordem decrescente, e as palavras mais frequentes foram exibidas:

```python
palavras_ordenadas = contagem_palavras.orderBy(col("count").desc())
palavras_ordenadas.show()
```

![Imagem comandos pyspark](../evidencias/4-apache-spark-execucao-comandos.png)

8. **Resultado obtido**

![Imagem resultado script pyspark](../evidencias/5-apache-spark-resultado.png)

___

## 2. Lab AWS Glue
- O laboratório consiste em construir um processo de ETL simplificado utilizando AWS Glue.

### 1. Preparação dos dados de origem
- É um arquivo CSV com os nomes mais comuns de registro de nascimento dos cartórios americanos entre 1880 e 2014. Consiste em um arquivo CSV com o seguinte formato:

*nome,sexo,total,ano*
*Jennifer,F,54336,1983*

- O arquivo **deverá estar em um Bucket** do S3.
    - O caminho deve ser: s3://{BUCKET_NAME}/lab-glue/input/nomes.csv

**SOLUÇÃO**
- Primeiramente, criei o bucket com o nome **"lab-aws-glue-artur"**.
- Em seguida, fiz upload do arquivo para o bucket.
- Tudo isso utilizando o mesmo script da Sprint passada, porém realizando as alterações necessárias:
    - Modifiquei a key do S3 (caminho onde irá salvar no S3);
    - Modifiquei o nome do arquivo e do Bucket.

**EXECUÇÃO**
1. Script
![Imagem execução VSCode](../evidencias/1-lab-aws-glue-execucao.png)

2. AWS
![Imagem bucket criado e upload concluído](../evidencias/1-lab-aws-glue-execucao-aws1.png)


### 2. Configuração da conta para usar AWS Glue
- Deve-se prover acesso total ao S3 para leitura e escrita.

**EXECUÇÃO**
- Ao selecionar a opção de selecionar usuários, não possuía nenhum. Com isso, criei um usuário IAM para este exercício (**user-glue**).

![Imagem sem usuários encontrados](../evidencias/2-lab-aws-glue-select-usuario.png)

![Imagem criação usuário IAM](../evidencias/2.1-lab-aws-glue-setup-users.png)


### 3. Criação de IAM Role para os jobs do AWS Glue
- Após isso, tornou-se necessária a criação de credenciais temporárias - *roles*.
- Bastou seguir o passo a passo conforme imagens abaixo.

![Imagem configuração roles](../evidencias/3-lab-aws-glue-conf-roles.png)
![Imagem configuração roles 2](../evidencias/3.1-lab-aws-glue-conf-roles.png)
![Imagem configuração roles 3](../evidencias/3.2-lab-aws-glue-conf-roles.png)


### 4. Configuração das permissões no AWS Lake Formation
- Primeiramente, criei o banco de dados **"glue-lab"**.

![Imagem criação banco de dados](../evidencias/4-lab-aws-glue-database-criado.png)

- Em seguida, alterei as permissões, concedendo ao usuário user-glue, criado conforme item 2 acima.

![Imagem adição administrador](../evidencias/4.1-lab-aws-glue-acesso-iam-user.png)
![Imagem garantia permissões](../evidencias/4.2-lab-aws-glue-conf-database.png)

### 5. Criação de job no AWS Glue
- Primeiramente criei o job conforme requerido no pdf [glue-lab](glue-lab.pdf).

![Imagem criação job](../evidencias/5-lab-aws-glue-create-job.png)


- Em seguida, realizei o teste fornecido como exemplo:

![Imagem job](../evidencias/5.1-lab-aws-glue-script-job.png)

Para isso, necessitei alterar os parâmetros S3_INPUT_PATH e S3_TARGET_PATH, sendo eles o caminho para o arquivo movies.csv, no bucket criado para o desafio final, e o destino inseri no próprio bucket criado para o presente exercício, fornecendo o caminho s3://<bucket>/lab-glue/output/.

![Imagem execução bem sucedida](../evidencias/5.1.2-lab-aws-glue-job-run-succeeded.png)
![Imagem execução arquivos](../evidencias/5.1.3-lab-aws-glue-job-run-succeeded.png)



___

### ↩️ [Retornar ao início](../../README.md)