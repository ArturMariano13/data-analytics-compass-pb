# 📈 Evidências do desafio da Sprint 3
Necessitei fazer o download das bibliotecas pandas e matplotlib, além da extensão do Jupyter para o VSCode. Como nunca havia tido contato com tratamento de dados, busquei materiais na web e contei com a ajuda da monitora Taise para me auxiliar nesse processo.

## 🔍 Passo a passo
### 1. Leitura e Tratamento de Dados
**📝 LEITURA**

Primeiramente fiz a leitura dos dados utilizando a biblioteca `pandas` e utilizando um *dataframe* conforme pode ser percebido em [Leitura csv](1_leitura.png).

**🔧 TRATAMENTO**

**1.1 Correção de tipos incorretos**
- ***Reviews*:** É do tipo *string*, mas deve ser um valor inteiro.
    - [Verificando Reviews](1_tratamento_reviews1.png)
    - [Erro na linha 10472](1_tratamento_reviews2.png)
    - [Conversão de tipo Reviews](1_tratamento_reviews3.png)
- ***Size*:** É do tipo *string*, mas deve ser um valor *float*.
    - [Verificando Size](1_tratamento_size1.png)
    - [Corrigindo tipo Size](1_tratamento_size2.png)
- ***Installs*:** É do tipo *string*, mas deveria ser um valor inteiro.
    - [Verificando Installs](1_tratamento_installs1.png)
    - [Corrigindo campo](1_tratamento_installs2.png)
- ***Price*:** É do tipo *string*, mas deveria ser um valor *float*.
    - [Verificando Price](1_tratamento_price1.png)
    - [Corrigindo campo](1_tratamento_price2.png)
- ***Last Updated*:** É do tipo *string*, mas deveria ser do tipo *datetime*.
    - [Verificação e correção Last Updated](1_tratamento_lastupdated.png)

**1.2 Correção de dados *missing***
- [Identificação](1_tratamento_missing1.png)
- [Rating nulos](1_tratamento_missing_rating.png)
- [Size e Type nulos](1_tratamento_missing_size_type.png)
- [Current Ver & Android Ver](1_tratamento_missing_version.png)

**1.3 Eliminação de duplicados**
- [Remoção de duplicados](1_tratamento_nodups.png)

### 2. Gráfico de barras com os top 5 apps por número de instalação
Primeiramente, ordenei o *dataframe* de forma decrescente de acordo com o número de instalações. Vale ressaltar que, realizando alguns testes, percebi a presença de diversos *apps* com a mesma quantidade de downloads dos top 5. Com isso, optei por realizar uma segunda ordenação, por ordem alfabética. Após isso, armazenei em nova variável os 5 primeiros registros utilizando o `.head(5)`.
- [Código](ex2_codigo.png)
- [Gráfico](ex2_grafico.png)

### 3. Gráfico de pizza com frequência de categorias
Nesse caso, armazenei o total de categorias e o percentual de cada uma delas. Realizando um teste dessa forma, o gráfico ficou bastante confuso, com diversas categorias sobrepostas uma a outra.

Com isso, optei por criar uma categoria chamada "outras", a qual possui todas as categorias cujos percentuais ficaram abaixo dos 2%. Dessa forma, ficou mais claro o gráfico.
- [Código](ex3_codigo.png)
- [Gráfico](ex3_grafico.png)

### 4. App mais caro
Para solucionar esse exercício, busquei no dataset o maior *Price*. Por meio da função `idxmax()` encontrei o índice, e depois por meio da função `.loc()` encontrei o registro no dataset.
- [Código](ex4.png)

### 5. Quantidade de apps "Mature 17+"
Neste exercício, criei um laço de repetição que percorreu o *dataframe*, verificando registros em que o *Content Rating* fosse igual a "Mature 17+", contando os registros e armazenando em uma variável `count`.
- [Código](ex5.png)

### 6. Top 10 apps por número de *reviews*
A resolução desse exercício baseou-se na ordenação decrescente do *dataframe* a partir do número de *reviews*. Por meio da função `.head(10)` busquei os 10 primeiros registros.
- [Código](ex6.png)

### 7. Criação de dois cálculos sobre o dataset (lista e valor)
#### 7.1. Lista: Top 10 apps com atualização mais recente
Uma vez que o campo data já havia sido convertido para o tipo *date*, bastou ordenar de forma decrescente e buscar os dez primeiros registros.
- [Código](ex7.1.png)

#### 7.2 - Valor: App com mais instalações da categoria GAMES
O procedimento para realizar esse exercício foi: buscar todos os apps da categoria GAMES, busca o índice máximo (bem como no exercício 4) e busca do app com maior número de instalações pelo índice encontrado (função `loc()`).
- [Código](ex7.2.png)

### 8. Criação de outras duas formas de representação gráfica
#### 8.1. Gráfico de linha (*Installs* X *Last Updated*)
O objetivo deste gráfico é relacionar o número de instalações dos aplicativos com a data de sua última atualização. Observou-se uma tendência em que aplicativos com um maior número de instalações tendem a ter uma data de atualização mais recente. Para esta análise, escolheu-se o ano de 2018, pois foi o último ano com registros disponíveis no dataset e também o ano com o maior número de aplicativos registrados.
- [Código](ex8.1_codigo.png)
- [Gráfico](ex8.1_grafico.png)

#### 8.2. Gráfico de dispersão (*Rating* X *Reviews*)
Esse gráfico faz uma comparação entre a avaliação (de 0 a 5) e o número de reviews, podendo perceber qual é a relação entre essas duas grandezas.
- [Código](ex8.2_codigo.png)
- [Gráfico](ex8.2_grafico.png)

### 🔗 Links importantes utilizados
- [Biblioteca Pandas](https://www.w3schools.com/python/pandas/default.asp)
- [Biblioteca Matplotlib](https://www.w3schools.com/python/matplotlib_pyplot.asp)
- [Análise de Dados com Python](https://www.youtube.com/watch?v=gtjxAH8uaP0)

### ↩️ [Retornar ao início](../../../README.md)
