# Exercícios da Sprint 7
Este diretório contém os exercícios da Sprint 7. 

São dois (2) exercícios: Laboratório de AWS Glue e outro envolvendo a criação de um contador de palavras com Apache Spark.

## 1. Apache Spark - Contador de Palavras
- **Resumo:** 
- [Arquivos]()
- [Resolução completa]()


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
- Ao selecionar a opção de selecionar usuários, não possuía nenhum. Com isso, criei um usuário IAM para este exercício.

___

### ↩️ [Retornar ao início](../../README.md)