# SPRINT 3 - Python e Introdução AWS

## Certificados
Para maiores informações sobre os certificados, siga o link: [certificados](certificados)

## Desafio
Para maiores informações sobre o desafio final, siga o link: [desafio](desafio)

## Evidências
Para maiores informações sobre as evidências, siga o link: [evidências](evidencias)

## Exercícios
Para maiores informações sobre os exercícios, siga o link: [exercícios](exercicios)


## Resumo dos estudos

### Python 🐍

#### Introdução
- Linguagem de Programação mais utilizada 🌎.
- Fácil aprendizado.
- Alto nível.
- **Vantagens**
    - Desenvolvimento web, APIs
    - Inteligência Artificial
    - *Big Data*
    - *Data Science*
- **PEP 8:** guia de estilos de codificação para Python.

##### Estruturas de Dados
- Regras para organizar dados.
- Exemplos: listas, árvores, filas, pilhas...

#### Fundamentos
##### Tipos básicos
- Boolean: `True` ou `False`
- Float: números com ponto flutuante (2.2);
- *String*: `print('Hello World!')`
- Lista: `[1,2,3]`
- Dicionário: `{'nome': 'Pedro', 'idade': 29}`
- *None*: tipo indefinido, sem valor.

##### Variáveis
- Python é uma linguagem **dinamicamente tipada** => variáveis podem ter o seu tipo alterado.

##### Comentários
`# comentario de linha`
- Para múltiplas linhas, utiliza-se """ no começo e ao final, simulando uma string.
- Em um contexto educacional, utilizar.
- Profissionalmente, em geral, evitar. Utilizar nomes claros para variáveis, funções; boas práticas de programação.

##### Operadores Aritméticos
- `2 + 3` = soma (5)
- `5 - 8` = subtração (-3)
- `2 * 5.3` = multiplicação (10.6)
- `9.4 / 3` = divisão (3.133333333)
- `9.4 // 3` = divisão com resultado inteiro (3.0)
- `2 ** 8` = potenciação (256)
- `10 % 3` = módulo (resto da divisão) (1)

##### Operadores Relacionais
- Resposta é verdadeira ou falsa.
- `>` - maior que
- `<`- menor que
- `>=` - maior ou igual a
- `<=` - menor ou igual a
- `==` - igual a
- `!=` - diferente de

##### Operadores de Atribuição
- `a = 3` - "a recebe 3"
- `a = a + 7` - "a recebe ele mesmo mais 7" (a = 10)
- `a += 5` - igual ao exemplo de cima

- OBS.: O mesmo serve para as operações de `-`, `*`, `/`, `%`, `**`, `//`.

##### Operadores Lógicos
- `True or False`
- `7 != 3 and 2 > 3`
- `&`, `|` e `^` funcionam, porém comparam bit a bit.

##### Operadores Ternários
- Exemplo 1: 
``` python
esta_chovendo = True
'As roupas do varal estão ' + ('secas.', 'molhadas.')[esta_chovendo]
```
    - Nesse caso, secas será exibido se esta_chovendo for False, e molhadas será exibido quando esta_chovendo for True.
- Exemplo 2:
```python
esta_chovendo = True
'As roupas do varal estão ' + ('molhadas.' if esta_chovendo else 'secas.')
```
    - Esse exemplo possui a mesma lógica do exemplo 1.

##### Operador Membro
- Verifica se um elemento é membro de uma estrutura.
```python
lista = [1, 2, 3, 'Ana', 'Carla']
2 in lista # True
'Ana' not in lista # False
```

##### Operador Identidade
- Verifica se um termo é igual a outro.
```python
x = 3
y = x
z = 3
x is y # True
y is z  # True
x is not z # False
```

##### Builtins
É de onde vem as funções "type", "print", os tipos "int", "bool"...
```python
__builtins__.type('Bom dia') # irá retornar str
__builtins__.print(10 / 3) # irá printar 3.3333333
```

OBS.: comando `dir()` mostra o escopo global como estrutura de diretórios. Tudo o que for criado estará ali.

##### Conversão de Tipos
Formato: tipo(variável a ser modificada).
- Exemplo:
```python
a = 2
b = '3'

print(a + int(b)) # 5
```

##### Correção automática
Algumas correções que o Python realiza automaticamente para ajudar os desenvolvedores.
- Divisões geralmente serão do tipo *float*, mesmo que o resultado seja inteiro.
- `2 + True` = 2

##### Tipos Numéricos
- int, float, decimal
- `is_integer()` - retorna True ou False.
- `__abs__()` - retorna o valor absoluto (módulo).
- **Decimal:** garante mais precisão. Junto ao getcontext ele permite escolher quantas casas decimais utilizar.
    ```python
    from decimal import Decimal, getcontext

    Decimal(1) / Decimal(7)

    getcontext().prec = 4
    Decimal(1) / Decimal(7) # resposta com 4 casas decimais

    Decimal.max(Decimal(1), Decimal(7)) # retorna o maior deles: 7
    ```

##### String
O tipo *str* serve para lidar com cadeias de texto, e entre os tipos básicos é um dos que mais métodos e recursos possui.
- Os caracteres de uma string estão indexados.
- Não se pode fazer atribuições a uma string. Ela é **imutável**.
- Texto com múltiplas linhas - utiliza-se três aspas duplas => """.
- '\n' é quebra de linha.
- **Índices**
    ```python
    nome = 'Artur Mariano'
    nome[0] # 'A'
    nome[-3] # 'a'
    nome[6:] # tudo a partir do 6º caracter: 'Mariano'
    nome[2:5] # 'tur'
    nome[::-1] # inverte a string
    ```
- **Algumas funções**
    ```python
    frase = 'Python é uma excelente linguagem'
    'py' in frase # retorna False pois é case-sensitive
    len(frase) # retorna o tamanho da string frase
    
    frase.lower() # transforma tudo para letra minúscula
    frase.upper() # transforma tudo para letra maiúscula

    frase.split() # divide nos espaços em branco
    frase.split('A') # divide onde tiver a letra 'A'
    ```

##### Listas
Uma lista é similar a uma *array*, porém ela vai muito além disso. As listas **não são tipadas**, ou seja cada elemento pode ser de um tipo diferente.
- *Slicing* - permite formas extremamente poderosas de acesso aos seus elementos. 

```python
lista = []
len(lista) # retorna o tamanho da lista
lista.append(1) # insere um elemento ao final da lista

nova_lista = [1, 2, 3, 'Pedro', 'Maria']
nova_lista.remove(3)
nova_lista.reverse() # inverte a lista
1 in lista # True

```

##### Tuplas
As tuplas são similares a lista porém elas são imutáveis, e portanto não podem receber alterações. Existem algumas situações em que uma tupla pode ser preferida a uma lista, uma delas é como chave em um dicionário.

##### Dicionários
Estruturas de chave e valor.
```python
pessoa = {'nome' : 'Ana', 'idade' : 25, 'cursos' : ['Inglês', 'Python']}

pessoa['nome'] # retorna 'Ana'
pessoa['cursos'] # retorna os cursos
pessoa['cursos'][1] # retorna Python
pessoa.keys() # retorna as chaves (nome, idade, cursos)
pessoa.values() # retorna os valores (Ana, 25, [Inglês, Português])

```
##### Conjuntos
Os conjuntos são similares as listas, porém possui diferenças marcantes:
- Elementos únicos
- Não indexado
- Não ordenado
- Todos os elementos precisam ser imutáveis (não aceita dicionários e listas por exemplo)
- Possui diversos métodos baseado em lógica matemática de conjuntos (interseção, união, pertence, etc).
```python
c1 = {1, 2}
c2 = {2, 3}
c1.union(c2) # {1, 2, 3}
c1.intersection(c2) # {2}
c1.update(c2) # {1, 2, 3}
```

##### Interpolação
```python
nome, idade = 'Ana', 30

# Forma 1
print('Nome: %s Idade: %d' % (nome, idade)) # irá substituir no lugar corretamente

# Forma 2
print(f'Nome: {nome} Idade: {idade}')
```

#### Estrutura de Controle


___

### AWS - Cloud Economics
4 pilares:
- Redução de custos
- Produtividade da equipe
- Resiliência operacional
- Agilidade empresarial

#### MPA - Ferramenta de Planejamento de Migração para a Nuvem ☁️

A **MPA** é uma ferramenta da AWS que auxilia parceiros de consultoria em migrações para a nuvem, oferecendo análises de redução de custos 💰 e outros relatórios úteis 📊 para o planejamento da migração.

##### Funcionalidades Principais 🛠️

- **Análise de Inventário de TI**: Permite mapear recursos on-premises para serviços AWS, comparando custos entre os cenários.
- **Validação de Caso de Negócios**: Ajuda a criar planos de migração detalhados, incluindo esforço necessário, custos associados e fluxo de caixa 📈.
- **Priorização de Migrações**: Facilita a análise e priorização correta das migrações de aplicativos 📋.

##### Uso nos Estágios Iniciais do Projeto 🚀

A MPA pode ser usada no início do projeto para detalhar a infraestrutura de cada servidor ou aplicativo, tornando o planejamento mais claro e preciso 🔍.

##### Fatores de Viabilidade do Projeto 📝

A MPA ajuda a determinar os seguintes fatores:

- **Avaliação do Custo Total de Propriedade (TCO)**: Estima a redução de custos 💸.
- **Comparações de Infraestrutura**: Entre on-premises e AWS.
- **Estimativa de Custos do Projeto**: Projeções financeiras da migração 📊.
- **Recomendações de Dimensionamento**: Para migrações do tipo Rehospedagem (lift-and-shift).

##### Benefícios para o Planejamento 📅

A MPA fornece uma base sólida para o planejamento da migração, agrupando e priorizando ondas de migração de aplicativos e servidores.

---



