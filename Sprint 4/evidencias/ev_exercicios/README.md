# Evidências dos Exercícios da Sprint 4
Os exercícios desta *sprint* consistiram em atividades de programação (Python), utilizando conceitos da Programação Funcional, e todos eles foram realizados pelo ambiente da Udemy.

## Exercício 1
Você está recebendo um arquivo contendo 10.000 números inteiros, um em cada linha. Utilizando **lambdas** e ***high order functions***, apresente os 5 maiores valores pares e a soma destes.

Você deverá aplicar as seguintes funções no exercício:
- `map`
- `filter`
- `sorted`
- `sum`

Seu código deverá exibir na saída (simplesmente utilizando 2 comandos `print()`):
- a lista dos 5 maiores números pares em ordem decrescente;
- a soma destes valores.

### Solução
1- Ler o arquivo e converter cada linha em um número inteiro usando `map` e `list`.
2- Filtrar os valores e selecionar apenas os pares, utilizando `filter`.
3- Ordenar os números pares em ordem decrescente utilizando `sorted`.
4- Calcular a soma dos 5 maiores utilizando `sum`.
5- *Prints* necessários.
- [Código](../../exercicios/exer1.py)
- [Evidência exer1](exer1.png)

## Exercício 2
Utilizando *high order functions*, implemente o corpo da função `conta_vogais`. O parâmetro de entrada será uma *string* e o resultado deverá ser a contagem de vogais presentes em seu conteúdo.

É obrigatório aplicar as seguintes funções:
- `len`
- `filter`
- `lambda`

Desconsidere os caracteres acentuados. Eles não serão utilizados nos testes do seu código.

### Solução
1- Definir as vogais 'aeiou'
2- Percorrer a *string* recebida por parâmetro e contar as vogais utilizando `filter` e `lambda`
3- Retornar o tamanho da lista criada
- [Código](../../exercicios/exer2.py)
- [Evidência exer2](exer2.png)

## Exercício 3
A função `calcula_saldo` recebe uma lista de tuplas, correspondendo a um conjunto de lançamentos bancários. Cada lançamento é composto pelo seu valor (sempre positivo) e pelo seu tipo (C - crédito ou D - débito). 

A partir dos lançamentos, a função deve calcular o valor final, somando créditos e subtraindo débitos. Na lista anterior, por exemplo, teríamos como resultado final 200.

Além de utilizar `lambdas`, você deverá aplicar, obrigatoriamente, as seguintes funções na resolução:
- `reduce` (módulo functools)
- `map`


### Solução 
1- Armazena os lançamentos (tuplas) nas variáveis valor e tipo.
2- Por meio de `map`, percorre os lançamentos e verifica se o tipo é 'C' para retornar valor positivo, o contrário retorna negativo.
3- Converter para lista.
4- O saldo recebe um acumulador, que inicia em 0, por meio da função `reduce`.
- [Código](../../exercicios/exer3.py)
- [Evidência exer3](exer3.png)

## Exercício 4
A função `calcular_valor_maximo` deve receber dois parâmetros, chamados de operadores e operandos. Em operadores, espera-se uma lista de caracteres que representam as operações matemáticas suportadas **(+, -, /, *, %)**, as quais devem ser aplicadas à lista de operadores nas respectivas posições. Após aplicar cada operação ao respectivo par de operandos, a função deverá retornar o maior valor dentre eles.

Na resolução da atividade você deverá aplicar as seguintes funções:
- `max`
- `zip`
- `map`

### Solução
1- Um dicionário operacoes mapeia operadores (+, -, *, /, %) para funções `lambda` que realizam as respectivas operações.
2- A função interna `aplicar_operacao` aplica uma operação (extraída de operadores) a um par de operandos (extraído de operandos).
3- Usa `zip` para combinar operadores e operandos em pares, e `map` para aplicar cada operação.
4- `max` encontra o maior valor resultante das operações.
- [Código](../../exercicios/exer4.py)
- [Evidência exer4](exer4.png)

## Exercício 5
Um determinado sistema escolar exporta a grade de notas dos estudantes em formato CSV. Cada linha do arquivo corresponde ao nome do estudante, acompanhado de 5 notas de avaliação, no intervalo [0-10]. É o arquivo estudantes.csv de seu exercício.

Precisamos processar seu conteúdo, de modo a gerar como saída um relatório em formato textual contendo as seguintes informações:
- Nome do estudante
- Três maiores notas, em ordem decrescente
- Média das três maiores notas, com duas casas decimais de precisão

O resultado do processamento deve ser escrito na saída padrão (print), ordenado pelo nome do estudante e obedecendo ao formato descrito a seguir: **Nome: <nome estudante> Notas: [n1, n2, n3] Média: <média>**

Em seu desenvolvimento você deverá utilizar *lambdas* e as seguintes funções:
- `round`
- `map`
- `sorted`

### Solução
Vale ressaltar que nesse exercício tive dificuldades na realização, pois apesar de estar tendo o resultado esperado, a plataforma da Udemy não reconhecia como correta a saída.

Sendo assim, necessitei readaptar meu arquivo desde a leitura até o print para funcionar corretamente.
1- O arquivo CSV é aberto e lido. Cada linha é lida e separada em uma lista de strings, uma por linha.
2- A função `processar_linha` divide a linha em colunas, extrai o nome e converte as notas para inteiros. Utiliza `calcular_media_maiores_notas` para encontrar as três maiores notas e a média. Retorna uma tupla com o nome, maiores notas e média.
3- Usar `map` para aplicar `processar_linha` a cada linha do arquivo, resultando em uma lista de tuplas com os resultados. Em seguida, ordena a lista de tuplas por nome usando `sorted`.
4- Usar `map` para aplicar uma função lambda que imprime o nome, as maiores notas e a média de cada estudante.
- [Código](../../exercicios/exer5.py)
- [Evidência erro exer5](exer5_erro.png)
- [Evidência exer5 correto](exer5.png)

## Exercício 6
Você foi encarregado de desenvolver uma nova feature  para um sistema de gestão de supermercados. O analista responsável descreveu o requisito funcional da seguinte forma:
- Para realizar um cálculo de custo, o sistema deverá permitir filtrar um determinado conjunto de produtos, de modo que apenas aqueles cujo valor unitário for superior à média deverão estar presentes no resultado.
- Observe que estamos definindo a assinatura de uma função como parte de sua resposta. Você não pode mudá-la, apenas codificar seu corpo. O parâmetro conteudo é um dicionário cuja chave contém o nome do produto e o valor, o respectivo preço (ponto flutuante).
- O retorno da função obrigatoriamente deve ser uma lista. Cada elemento da lista é uma tupla em que a primeira posição contém o nome do produto e a segunda, o respectivo preço.

**Importante:** O retorno da função deve estar ordenado pelo preço do item (ordem crescente).

### Solução
1- Para **converter o dicionário para uma lista de tuplas**, utiliza-se `zip` para combinar as chaves (nomes dos produtos) e os valores (preços) do dicionário.
2- O **cálculo da média dos preços** foi calculado dividindo a soma dos preços por o número de produtos no dicionário. `conteudo.values()` fornece os preços, `sum` calcula a soma e `len` dá o número total de produtos.
3- Para a **filtragem dos produtos acima da média**, utiliza-se `filter` e uma função *lambda* para selecionar apenas os produtos cujo preço é maior que a média calculada. A função lambda `lambda x: x[1] > media` verifica se o preço (x[1]) é maior que a média.
4- A **ordenação dos resultados** é realizada com base no preço, em ordem crescente, usando `sorted` e a função `lambda x: x[1]` para definir a chave de ordenação. 
- [Código](../../exercicios/exer6.py)
- [Evidência exer6](exer6.png)

## Exercício 7
Generators são poderosos recursos da linguagem Python. Neste exercício, você deverá criar o corpo de uma função, cuja assinatura já consta em seu arquivo de início `(def pares_ate(n:int):)`.

O objetivo da função `pares_ate` é retornar um generator para os valores pares no intervalo [2,n]. Observe que n representa o valor do parâmetro informado na chamada da função.

### Solução
1- A função recebe um único argumento, n, que é o limite superior do intervalo (inclusive).
2- O loop `for` itera sobre todos os números no intervalo de 2 até n (inclusive). `range(2, n + 1)` gera números começando de 2 até n.
3- O if verifica se o número i é par. Isso é feito verificando se o resto da divisão de i por 2 (i % 2) é igual a 0.
4- Quando a condição if é verdadeira (ou seja, i é par), yield é usado para gerar o valor i. Diferentemente de return, que termina a execução da função, `yield` permite que a função retorne um valor e continue sua execução a partir do ponto onde foi interrompida, permitindo que o gerador produza mais valores conforme necessário.
- [Código](../../exercicios/exer7.py)
- [Evidência exer7](exer7.png)

___

### ↩️ [Retornar ao início](../../../README.md)