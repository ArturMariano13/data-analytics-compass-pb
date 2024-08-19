# 🧩 Desafio da Sprint 5
Este diretório contém os arquivos necessários para a realização do desafio desta Sprint.

## 📝 Enunciado(s)
1. Procure um arquivo CSV ou JSON no portal de dados públicos do Governo Brasileiro: [link](http://dados.gov.br)
    - Garanta que seu arquivo seja único na turma;
    - Certifique-se de que não excedeu nenhum limite do S3 de acordo com a documentação do mesmo.

2. Analise o conjunto de dados escolhido localmente em editor de texto para conhecer os dados e o que pode ser analisado.

3. Carregue o arquivo para um *bucket* novo, para executar o desafio.

4. Você pode utilizar o **Console** (nota até 80%) ou desenvolver um código Python usando **Boto3** (nota até 100%) para fazer uso do S3 Select.

5. Através da função **S3 Select** crie pelo menos uma consulta no seu arquivo que utilize:
    1. Uma cláusula que filtra dados usando ao menos dois operadores lógicos
    2. Duas funções de agregação
    3. Uma função condicional
    4. Uma função de conversão
    5. Uma função de data
    6. Uma função de string

OBS.: menos consultas = maior avaliação

6. Armazenar no Git um arquivo Markdown explicando seu conjunto de Dados, bem como sua(s) consulta(s) e o resultado das execuções de suas consultas.
    - Armazenar a(s) consultas em arquivo(s) *.sql*
    - Armazenar o(s) arquivo(s) de código em arquivo(s) *.py*
    - Armazenar as evidências de execução com imagens *.jpeg* ou *.png*

## Resposta(s)
### 1. Escolha do conjunto de dados
Selecionei a base de dados da polícia federal com diversas operações realizadas em diferentes datas, com foco em tipos específicos de crimes e atividades.
- **Site do governo:** [link](https://dados.gov.br/dados/conjuntos-dados/palas---sistema-de-informacoes-de-investigacao)
- **Arquivo baixado:** [link](PALAS_OPERACOES_2024_01.csv)

### 2. Análise do conjunto de dados selecionado
- Markdown com análise do dataset: [Arquivo](analise_dados.md)

### 3. Carregar arquivo para bucket novo
Explicar processo de criação do bucket, carregamento...

### 4, 5. Criação do script Python com as consultas
**1º passo:** instalar biblioteca Boto3: `pip install boto3`

**2º passo:** configurar AWS.



- Código: [Arquivo](caminho)

___

### ↩️ [Retornar ao início](../../README.md)