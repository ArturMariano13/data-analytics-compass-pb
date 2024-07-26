# 📝 Evidências dos Exercícios da Sprint 3
Este arquivo está dividido em duas partes, bem como os exercícios da sprint 3:
1. Exercícios no ambiente da Udemy (práticos) - 25 exercícios
2. Exercício proposto (ETL) - tratamento de arquivo *actors.csv*

## Parte 1

### Exercício 1
- [Exercício 1](ex1.png)
- **Enunciado:** desenvolver um código em Python que crie variáveis para armazenar o nome e a idade de uma pessoa, juntamente com seus valores correspondentes. Como saída, deveria imprimir o ano em que a pessoa completará 100 anos de idade.
- **Resolução:** a resolução foi tranquila diante dos conhecimentos prévios e adquiridos com o curso. Utilizei a biblioteca datetime para buscar o ano atual, podendo reutilizar esse código quando necessário.

### Exercício 2
- [Exercício 2](ex2.png)
- **Enunciado:** Escreva um código Python que use a função range() para adicionar três números em uma lista(Esta lista deve chamar-se 'números')  e verificar se esses três números são pares ou ímpares. Para cada número, imprima como saída Par: ou Ímpar: e o número correspondente (um linha para cada número lido). Importante: Aplique a função range() em seu código.
- **Resolução:** para realizar o exercício 2, utilizei a função range e um laço for que realizava três iterações (de 3 a 5) e inseria os três valores na lista "numeros". Com isso, a saída foi: 
```python
Ímpar: 3
Par: 4
Ímpar: 5
```

### Exercício 3
- [Exercício 3](ex3.png)
- **Enunciado:** Escreva um código Python para imprimir os números pares de 0 até 20 (incluso). Importante: Aplique a função range() em seu código. 
- **Resolução:** a resolução desse exercício foi bem simples, com apenas três linhas de código. Bastou implementar um laço for com `for i in range(21)`, com o número 21, pois ele realiza iterações partindo do 0 (*default*) e terminando um número antes do fim do range (nesse caso, 20).

### Exercício 4
- [Exercício 4](ex4.png)
- **Enunciado:** Escreva um código Python para imprimir todos os números primos entre 1 até 100. Lembre-se que você deverá desenvolver o cálculo que identifica se um número é primo ou não. Importante: Aplique a função range().
- **Resolução:** para solucionar esse exercício, lembrei de uma tarefa que fiz para a faculdade na disciplina de Algoritmos II. Quando fiz, utilizamos a linguagem C++ e necessitamos utilizar do conceito de recursividade. Nesse caso, bastou **tentar realizar a divisão de um número x do 2 e indo até ele próprio - 1**. Caso alguma divisão fosse realizada, um contador era incrementado e aquele número não era primo.

### Exercício 5
- [Exercício 5](ex5.png)
- **Enunciado:** Escreva um código Python que declara 3 variáveis: *dia*, inicializada com valor 22; *mes*, inicializada com valor 10; *ano*, inicializada com valor 2022. Como saída, você deverá imprimir a data correspondente, no formato a seguir dia/mes/ano.
- **Resolução:** esse exercício também tem uma resolução bastante simples, sendo necessário apenas atribuir às três variáveis os seus respectivos valores, e concatenando com "/" para formar a data no formato desejado.

### Exercício 6
- [Exercício 6](ex6.png)
- **Enunciado:** Recebemos duas listas distintas, e deveríamos escrever um programa para avaliar o que ambas as listas têm em comum (sem repetições), imprimindo a lista de valores da interseção na saída padrão. Importante:  deveríamos utilizar o construtor `set()` em seu código.
- **Resolução:** primeiramente pensei em percorrer ambas as listas e, quando encontrasse algum valor igual nas duas listas, inseria em uma terceira. Contudo, creio que essa lógica se aplique para linguagens mais baixo nível, como C/C++. Em Python, o método `set()` realiza isso sozinho. Com isso, ao entender como ele funcionava, resolvi o problema em apenas uma linha de código.

### Exercício 7
- [Exercício 7 - primeira versão](ex7.1.png) 
- [Exercício 7 - versão final](ex7.2.png)
- **Enunciado:** Dada a seguinte lista: `a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]`, faça um programa que gere uma nova lista contendo apenas números ímpares.
- **Resolução:** nesse exercício eu realizei duas versões. A primeira foi utilizando os conceitos que eu já detinha. Nesse sentido, desenvolvi um laço for que percorria a lista e inseria em outra os valores ímpares. Contudo, no curso da Udemy há uma seção de *list comprehension* que mostra como fazer esse processo de preencher uma lista em apenas uma linha. Fazendo isso, simplifiquei o código e reduzi ele.

### Exercício 8
- [Exercício 8](ex8.png) 
- **Enunciado:** Verifique se cada uma das palavras da lista ['maça', 'arara', 'audio', 'radio', 'radar', 'moto'] é ou não um palíndromo. Obs: Palíndromo é uma palavra que permanece igual se lida de traz pra frente.
- **Resolução:** para realizar esse exercício utilizei uma técnica também aprendida no curso da Udemy, de colocar [::-1] ao lado de cada item da lista (como se fosse um índice), visto que o '-' faz ela ser invertida. Em uma linguagem de mais baixo nível, utilizaria de laços de repetição para realizar essa tarefa.

### Exercício 9
- [Exercício 9](ex9.png)
- **Enunciado:** Dadas três listas com primeiros nomes, sobrenomes e idades, faça um programa que imprima o dados na seguinte estrutura: "índice - primeiroNome sobreNome está com idade anos".
- **Resolução:** para resolver esse exercício, utilizei a função `enumerate` e a função `zip`. A primeira foi utilizada para obter um índice junto com cada tupla, as quais foram formadas pela função `zip` (junta as três listas em uma sequência de tuplas).

### Exercício 10
- [Exercício 10](ex10.png)
- **Enunciado:** Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados.
- **Resolução:** novamente utilizei a função `set` do Python para resolver, pois ela elimina os repetidos.

### Exercício 11
- [Exercício 11](ex11.png)
- **Enunciado:** Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.
- **Resolução:** para solucionar este exercício, utilizei a função `with open`, para que abrisse o arquivo e, ao final da mesma, o fechasse. Com isso, bastou carregar o conteúdo em uma variável e imprimir na saída padrão. Necessitei utilizar da biblioteca json também.

### Exercício 12
- [Exercício 12](ex12.png)
- **Enunciado:** Implemente a função `my_map(list, f)` que recebe uma lista como primeiro argumento e uma função como segundo argumento. Esta função aplica a função recebida para cada elemento da lista recebida e retorna o resultado em uma nova lista. Teste sua função com a lista de entrada `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` e com uma função que potência de 2 para cada elemento.
- **Resolução:** a resolução foi bem tranquila, exigindo duas funções básicas, sendo que uma delas deveria ser parâmetro da outra.

### Exercício 13
- [Exercício 13](ex13.png)
- **Enunciado:** Escreva um programa que lê o conteúdo do arquivo texto arquivo_texto.txt e imprime o seu conteúdo.
- **Resolução:** para solucionar o exercício, necessitei utilizar novamente a função open, porém tive problemas na execução pela primeira vez, pois havia um espaço ao final de cada linha. Contudo, minha saída não estava exatamente igual, causando problemas. Para isso necessitei colocar o "fim" da linha.

### Exercício 14
- [Exercício 14](ex14.png)
- **Enunciado:** Escreva uma função que recebe um número variável de parâmetros não nomeados e um número variado de parâmetros nomeados e imprime o valor de cada parâmetro recebido.
- **Resolução:** nesse caso, necessitei utilizar os parâmetros _**kwargs_ e os _*args_ para realizar. Isso aprendi exclusivamente no curso, haja vista que nunca havia tido contato com tal forma de parâmetros.

### Exercício 15
- [Exercício 15](ex15.png)
- **Enunciado:** Implemente a classe Lampada. A classe Lâmpada recebe um booleano no seu construtor, Truese a lâmpada estiver ligada, False caso esteja desligada. A classe Lampada possuí os seguintes métodos: `liga()`: muda o estado da lâmpada para ligada, `desliga()`: muda o estado da lâmpada para desligada, `esta_ligada()`: retorna verdadeiro se a lâmpada estiver ligada, falso caso contrário.
- **Resolução:** para solucionar esse exercício, os conteúdos fornecidos pela Udemy foram suficientes para a realização do exercício. Primeiramente criei a classe com o devido atributo e os métodos necessários. Posteriormente, criei uma instância de Lâmpada e realizei os testes requeridos.

### Exercício 16
- [Exercício 16](ex16.png)
- **Enunciado:** Escreva uma função que recebe uma string de números separados por vírgula e retorne a soma de todos eles. Depois imprima a soma dos valores. A string deve ter valor  "1,3,4,6,10,76"
- **Resolução:** para resolver esse exercício, necessitei utilizar a função `split()` passando ',' como parâmetro, fazendo assim com que a string de entrada se tornasse uma lista contendo os números que estavam separados por vírgula.

### Exercício 17
- [Exercício 17 - 1ª versão](ex17.1.png)
- [Exercício 17 - 2ª versão](ex17.2.png)
- [Exercício 17 - 3ª versão](ex17.3.png)
- [Exercício 17 - 4ª versão](ex17.4.png)
- **Enunciado:** Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas: a lista recebida dividida em 3 partes iguais. Teste sua implementação com a lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]. 
- **Resolução:** na primeira tentativa não obtive êxito, pois a saída não foi a esperada. O retorno da função aparentemente retornou uma tupla, porém a resposta deve ser uma lista. A segunda tentativa não deu certo também. Tentei colocar três *prints* distintos, porém o Pyhton adiciona um '\n' ao final de cada um, ficando diferente do resultado esperado. A terceira tentativa também não obteve sucesso, pois não utilizei a função `len()`. Isso faz sentido para poder reutilizar o meu código, pois dada uma lista que não sei o tamanho, não seria adequada a minha primeira abordagem. Por fim, a **quarta versão** do exercício 17 obteve êxito, utilizando corretamente a função `len()`.

### Exercício 18
- [Exercício 18](ex18.png)
- **Enunciado:** Dado um dicionário, crie uma lista com todos os valores (não as chaves!) e coloque numa lista de forma que não haja valores duplicados.
- **Resolução:** neste exercício, utilizei de um conceito já utilizado anteriormente, de obter apenas itens não repetidos de uma lista (`set()`). Além disso, utilizei o método `.values()` para acessar apenas os valores do dicionário *speed*.

### Exercício 19
- [Exercício 19 - 1ª versão](ex19.1.png)
- [Exercício 19 - versão final](ex19.2.png)
- **Enunciado:** Calcule o valor mínimo, valor máximo, valor médio e a mediana da lista gerada. Obs.: devem ser utilizadas as funções `random` `sum` `min` `max`.
- **Resolução:** a minha primeira tentativa do exercício 19 não obteve sucesso, devido à saída personalizada que o exercício pede. Resolvendo isso, o meu código rodou corretamente.

### Exercício 20
- [Exercício 20](ex20.png)
- **Enunciado:** Imprima a lista abaixo de trás para frente `a = [1, 0, 2, 3, 5, 8, 13, 21, 34, 55, 89]`.
- **Resolução:** essa questão foi bem simples, sendo necessário apenas incluir o índice [::-1] para que a lista fosse impressa de trás para frente.

### Exercício 21
- [Exercício 21](ex21.png)
- **Enunciado:** Implemente duas classes, Pato e Pardal , que herdam de uma superclasse chamada Passaro as habilidades de voar e emitir som. Contudo, tanto Pato quanto Pardal devem emitir sons diferentes (de maneira escrita) no console, conforme o modelo a seguir.
- **Resolução:** o exercício em si não é tão complexo, no entanto exige entender como o Python trata a superclasse, que nesse caso é "Passaro".

### Exercício 22
- [Exercício 22](ex22.png)
- **Enunciado:** Crie uma classe chamada Pessoa, com um atributo privado chamado nome (declarado internamente na classe como `__nome`) e um atributo público de nome id. Adicione dois métodos à classe, sendo um para definir o valor de `__nome` e outro para retornar o valor do respectivo atributo.
- **Resolução:** a resolução do exercício é bastante simples, bastou verificar o link inserido no exercício proposto. Para resolver, necessitei incluir o `@property` em cima da função nome que atua como *getter* e `@nome.setter` acima da outra função nome, funcionando como *setter* do atributo nome.

### Exercício 23
- [Exercício 23](ex23.png)
- **Enunciado:** Crie uma classe Calculo que contenha um método que aceita dois parâmetros, X e Y, e retorne a soma dos dois. Nessa mesma classe, implemente um método de subtração, que aceita dois parâmetros, X e Y, e retorne a subtração dos dois (resultados negativos são permitidos).
- **Resolução:** na primeira vez que realizei este exercício, obtive um erro. Isso ocorreu, pois ele necessitava da criação de uma instância da classe para realizar as operações. Com isso, necessitei incluir o `@staticmethod` para poder executar sem a utilização do `self`.

### Exercício 24
- [Exercício 24](ex24.png)
- **Enunciado:** Crie uma classe Ordenadora que contenha um atributo listaBaguncada e que contenha os métodos ordenacaoCrescente e ordenacaoDecrescente. Instancie um objeto chamado crescente dessa classe Ordenadora que tenha como `listaBaguncada` a lista [3,4,2,1,5] e instancie um outro objeto, decrescente dessa mesma classe com uma outra `listaBaguncada` sendo [9,7,6,8]. Para o primeiro objeto citado, use o método `ordenacaoCrescente` e para o segundo objeto, use o método `ordenacaoDecrescente`.
- **Resolução:** esse exercício apresenta uma complexidade relativamente baixa, principalmente graças ao Python, que possui funções prontas de ordenação de listas. Com isso, foi simples resolver essa tarefa.

### Exercício 25
- [Exercício 25](ex25.png)
- **Enunciado:** Crie uma classe Avião que possua os atributos modelo, velocidade_maxima, cor e capacidade. Defina o atributo cor de sua classe , de maneira que todas as instâncias de sua classe avião sejam da cor “azul”. Após isso, a partir de entradas abaixo, instancie e armazene em uma lista 3 objetos da classe Avião. Ao final, itere pela lista imprimindo cada um dos objetos no seguinte formato: “O avião de modelo “x” possui uma velocidade máxima de “y”, capacidade para “z” passageiros e é da cor “w”. Sendo x, y, z e w cada um dos atributos da classe “Avião”.
- **Resolução:** esse exercício envolve diversos conhecimentos aplicados nos exercícios anteriores, porém todos juntos. Muito interessante entender como isso pode funcionar em uma aplicação maior. O único detalhe a ser cuidado consiste na atribuição de azul para todas as instâncias, não pedindo ao usuário informar a cor.

## Parte 2

**Preparação:** download do arquivo actors.csv, análise do arquivo e criação de arquivos .txt conforme requerido.
- [Preparação 1](ex_etl_0.png)

Após ler o exercício proposto, minha ideia inicial é realizar uma lista de dicionários contendo todas as informações. Assim, poderei realizar o tratamento diretamente na linguagem Python.
- [Leitura e criação de lista](ex_etl_1.png)

Percebi uma inconsistência na linha 5 do arquivo csv, o que exigiu um tratamento. O separador original, que deveria ser a vírgula, estava também no meio do nome do ator. Com isso, demandou-se um tratamento, conforme ilustrado na imagem. Assim sendo, a ideia citada acima não pôde ser concretizada.
- [Tratamento de erro na linha 5](ex_etl_2.png)

**Etapa 1:** para a realização da etapa 1, realizei um loop que percorreu a lista de dicionários criada, buscando o número de filmes de cada ator. Com isso, uma variável sofria modificações conforme o programa encontrava um ator que superava o anterior com mais filmes.
- [Etapa 1](ex_etl_3.png)

**Etapa 2:** para concluir essa etapa, criei uma variável para somar todos os valores de receita brutos e dividi pela quantidade de registros na lista criada, obtendo assim a média. Além disso, realizei o arredondamento para duas casas decimais, visando manter o padrão do próprio arquivo csv.
- [Etapa 2](ex_etl_4.png)

**Etapa 3:** a resolução dessa etapa do exercício é similar à etapa 1, exigindo apenas encontrar o maior dos valores nessa lista e, por meio do get, encontrar o nome do ator.
- [Etapa 3](ex_etl_5.png)

**Etapa 4:** a solução da etapa 4 necessitou de mais estudo da minha parte, pois necessitei realizar uma ordenação com dois parâmetros em caso de empate. Para isso, utilizei função *lambda* para solucionar, inserindo o parâmetro quantidade de aparições do filme como primeiro e nome (ordem alfabética) como segundo. Para isso, necessitei visitar alguns fóruns e sites com explicações, porém consegui solucionar. Vale ressaltar que o primeiro parâmetro possui um '-' antes dele, isto é, ele ordena em ordem decrescente a partir da quantidade de aparições.
- [Etapa 4](ex_etl_6.png)

**Etapa 5:** a etapa 5 era bastante similar à etapa anterior, o que facilitou o entendimento do que se tinha que fazer. Contudo, para resolvê-la, necessitei utilizar a função `sorted()` do Python com o parâmetro `reverse=True`, para que ordenasse corretamente de forma decrescente. Tanto nessa etapa, quanto na anterior, consultei o site da W3Schools [W3Schools - Lambda](https://www.w3schools.com/python/python_lambda.asp).
- [Etapa 5](ex_etl_7.png)

**Extra:** criei uma função também para a escrita dos resultados nos arquivos texto requeridos, conforme imagem do link abaixo.
- [Função escreve em arquivos](ex_etl_8.png)

- [**Resultado etapas 1, 2 e 3**](etl_res1.png)
- [**Resultado etapas 4 e 5**](etl_res2.png)
- [**Código:**](../../exercicios/parte-2-etl/script.py)

### ↩️ [Retornar ao início](../../../README.md)