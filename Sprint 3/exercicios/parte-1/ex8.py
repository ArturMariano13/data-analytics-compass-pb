"""
Verifique se cada uma das palavras da lista ['maça', 'arara', 'audio', 'radio', 'radar', 'moto'] 
é ou não um palíndromo.

Obs: Palíndromo é uma palavra que permanece igual se lida de traz pra frente.
"""

lista = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto'] 

for item in lista:
    if item[::-1] == item:
        print(f"A palavra: {item} é um palíndromo")
    else:
        print(f"A palavra: {item} não é um palíndromo")