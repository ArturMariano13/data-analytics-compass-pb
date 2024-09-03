# 🧩 Desafio da Sprint 6
Este diretório contém os arquivos necessários para a realização do desafio desta Sprint.

## Questões para Análise 

## 📝 Enunciado(s)
O desafio da Sprint 6 consiste na primeira entrega do desafio final, o qual terá cinco (5) sprints de duração (da 6ª até a 10ª).

Nesta sprint, devemos realizar a ingestão *batch* (em lote) dos arquivos CSV em um Bucket Amazon S3 RAW Zone.

Devemos desenvolver um código Python que será executado dentro de um container Docker para carregar os dados locais para a nuvem. Será amplamente utilizada a biblioteca `boto3` para a realização dessa etapa do desafio.

A imagem abaixo ilustra o que será realizado nessa primeira etapa do desafio.


![Imagem desafio](../evidencias/ev_desafio/0_imagem_desafio.png)

1. O código Python deve:
- **Ler** os dois (filmes e séries) no formato CSV **sem filtrar os dados**.
- Utilizar a lib **`boto3`** para **carregar os dados para a AWS**.
- Acessar a AWS e **gravar no S3**, no **bucket definido com RAW Zone**.
    - Na gravação dos dados, deve-se considerar o padrão: `<nome-do-bucket>\<camada-de-armazenamento>\<origem-dado>\<formato-do-dado>\<especificação-do-dado>\<data-do-processamento ano\mes\dia>\<arquivo>`.
        - Exemplo: `S3:\\data-lake\Raw\Local\CSV\Movies\2024\09\03\movies.csv` & `S3:\\data-lake\Raw\Local\CSV\Series\2024\09\03\series.csv`

2. Criar container Docker com um volume para armazenar os arquivos CSV e executar processo Python implementado.
3. Executar localmente o container Docker para realizar a carga dos dados ao S3.


___

### ↩️ [Retornar ao início](../../README.md)