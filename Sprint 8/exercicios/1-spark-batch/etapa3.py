import random
import time
import os
import names

random.seed(time.time())

qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

aux = []

for i in range(0, qtd_nomes_unicos):
    aux.append(names.get_full_name())

print(f"Gerando {qtd_nomes_aleatorios} nomes aleatórios")

dados = []

for i in range(0, qtd_nomes_aleatorios):
    dados.append(random.choice(aux))

file_name = 'nomes_aleatorios.txt'

if os.path.exists(file_name):
    print(f"Arquivo '{file_name}' já existe. Removendo o arquivo antigo.")
    os.remove(file_name)

with open(file_name, 'w') as file:
    for nome in dados:
        file.write(f"{nome}\n")

print(f"Arquivo '{file_name}' criado com sucesso!")
