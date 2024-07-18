"""
Escreva um programa que lê o conteúdo do arquivo texto arquivo_texto.txt e imprime o seu conteúdo.

Dica: leia a documentação da função open(...)
"""

filename = 'arquivo_texto.txt'

with open(filename, 'r') as file:
    for line in file:
        print(line, end='')

# Necessitei ler linha por linha, pois a Udemy não estava reconhecendo como correta minha solução prévia