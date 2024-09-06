"""
Escreva uma função que recebe uma string de números separados por vírgula e retorne a soma de todos eles. Depois imprima a soma dos valores.
A string deve ter valor  "1,3,4,6,10,76"
"""

def somaString(numeros):
    soma = 0
    for i in numeros.split(','):
        soma += int(i)
    return str(soma)

entrada = "1,3,4,6,10,76"

print(somaString(entrada))