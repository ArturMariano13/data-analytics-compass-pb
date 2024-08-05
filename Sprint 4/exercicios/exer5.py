# -*- coding: utf-8 -*-
def processar_estudantes(arquivo_csv):
    
    def calcular_media_tres_maiores(notas):
        maiores_notas = sorted(notas, reverse=True)[:3]
        return round(sum(maiores_notas) / len(maiores_notas), 2)
        
    def processar_linha(linha):
        partes = linha.strip().split(',')
        nome = partes[0]
        notas = list(map(int, partes[1:]))
        tres_maiores = sorted(notas, reverse=True)[:3]
        media = calcular_media_tres_maiores(tres_maiores)
        return {
            'nome': nome,
            'notas': tres_maiores,
            'media': media
        }

    with open(arquivo_csv, 'r', encoding='utf-8') as file:
        linhas = file.readlines()
    
    estudantes = map(processar_linha, linhas)
    
    resultados_ordenados = sorted(estudantes, key=lambda x: x['nome'])
    
    for estudante in resultados_ordenados:
        nome = estudante['nome']
        maiores_notas = estudante['notas']
        media = estudante['media']
        print(f"Nome: {nome} Notas: {maiores_notas} Média: {media}")

filename = 'estudantes.csv'
processar_estudantes(filename)
