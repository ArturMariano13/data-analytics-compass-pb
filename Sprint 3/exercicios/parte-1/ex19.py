"""
Calcule o valor mínimo, valor máximo, valor médio e a mediana da lista gerada na célula abaixo:
Obs.: Lembrem-se, para calcular a mediana a lista deve estar ordenada!

Use as variáveis abaixo para representar cada operação matemática:
- mediana
- media
- valor_minimo 
- valor_maximo 

Importante: Esperamos que você utilize as funções abaixo em seu código:
- random
- max
- min
- sum
"""

import random

random_list = random.sample(range(500), 50)

random_list.sort()

tamanho = len(random_list)

if tamanho % 2 == 0:
    mediana = (random_list[tamanho // 2 - 1] + random_list[tamanho // 2]) / 2
else:
    mediana = random_list[tamanho // 2]

media = sum(i for i in random_list) / tamanho
valor_minimo = min(random_list)
valor_maximo = max(random_list)

print(f'Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}')