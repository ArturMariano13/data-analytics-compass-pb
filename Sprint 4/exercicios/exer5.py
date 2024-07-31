def calcular_media_maiores_notas(notas):
    maiores_notas = sorted(notas, reverse=True)[:3]
    media = round(sum(maiores_notas) / len(maiores_notas), 2)
    return maiores_notas, media

def processar_csv(arquivo_csv):
    with open(arquivo_csv, mode='r') as file:
        linhas = file.read().splitlines()
        
    def processar_linha(linha):
        colunas = linha.split(',')
        nome = colunas[0]
        notas = list(map(int, colunas[1:]))
        maiores_notas, media = calcular_media_maiores_notas(notas)
        return (nome, maiores_notas, media)
    
    estudantes = list(map(processar_linha, linhas))
    
    estudantes = sorted(estudantes, key=lambda x: x[0])
    
    _ = list(map(lambda estudante: print(f"Nome: {estudante[0]} Notas: {estudante[1]} Média: {estudante[2]}"), estudantes))

processar_csv('estudantes.csv')
