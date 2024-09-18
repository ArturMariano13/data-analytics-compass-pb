# 🧩 Desafio da Sprint 7
Este diretório contém os arquivos necessários para a realização do desafio desta Sprint.

---

## 📝 Enunciado
O desafio da Sprint 7 é uma continuação do desafio iniciado na Sprint anterior a esta (6), sendo a segunda entrega do desafio final.

Nesta Sprint, devemos realizar a ingestão de API, isto é, capturar dados do TMDB a fim de complementar os dados carregados na Sprint anterior.

Esse processo de ingestão deve ser realizado via AWS Lambda, o qual deve realizar chamadas de API. Por conseguinte, os dados coletados devem ser persistidos em Amazon S3, camada RAW Zone, mantendo o formato da origem (JSON) e agrupando-os em arquivos com, no máximo, 100 registros cada arquivo.

Caso desejemos, podem ser utilizadas outras APIs de nossa escolha. 

### :warning: Informações importantes
- Os arquivos CSV carregados na Etapa 1 não devem ser modificados em nenhuma etapa do desafio.
- Os novos dados devem ser complementares aos dados do CSV.
- Não é necessário realizar o tratamento dos dados externos, o máximo que pode ser feito é o agrupamento de dados para gerar menor quantidade de arquivos JSON.
- Cuidado para os arquivos JSON gerados não serem maiores do que 10 MB.
- Não agrupar JSON com estruturas diferentes.
- Os IDs do IMDB presentes nos arquivos CSV podem ser utilizados em pesquisas do TMDB.
- Considere desenvolver seu código localmente primeiro e com poucos dados para depois levá-lo para a AWS Lambda.

Realizar as seguintes atividades:
1. Se necessário criar nova camada (*layer*) no AWS Lambda para as libs necessárias à ingestão de dados (por exemplo, *tmdbv3api*, se utilizar o TMDB).
2. Implementar o código Python em AWS Lambda para consumo de dados do TMDB.
3. Se está utilizando TMDB, buscar pela API os dados que complementem a análise. Se achar importante, agrupar os retornos da API em arquivos JSON com, no máximo, 100 registros cada.
4. Utilizar a lib `boto3` para gravar dados no AWS S3.
    - No momento da gravação dos dados deve-se considerar o padrão de *path*: `S3:\\data-lake-do-fulano\Raw\TMDB\JSON\ano\mes\dia\arquivo.json`.

## Resolução
### Novas questões para análise
Primeiramente, em conversas com o monitor da Sprint, optei por modificar as questões de análise por mim escolhidas na Sprint 6. Percebi que havia levantado muitas informações e desejava contar sobre vários filmes de Christopher Nolan, ao invés de focar em menos elementos do diretor, podendo realizar uma análise mais aprofundada.

Com isso, minha questão de análise atual são:

1. Quais foram os principais marcos que consolidaram Christopher Nolan como um dos diretores mais influentes do cinema mundial?
___

### ↩️ [Retornar ao início](../../README.md)