"""
Escreva um código Python para imprimir todos os números primos entre 1 até 100. 
Lembre-se que você deverá desenvolver o cálculo que identifica se um número é primo ou não.

Importante: Aplique a função range().
"""

for i in range(2, 101):
    cont = 0
    for j in range(2, i):
        if i % j == 0:
            cont += 1
            break
    if cont == 0:
        print(i)
