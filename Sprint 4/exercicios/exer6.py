def maiores_que_media(conteudo: dict) -> list:
    produtos = list(zip(conteudo.keys(), conteudo.values()))

    media = sum(conteudo.values()) / len(conteudo)

    resultado = list(filter(lambda x: x[1] > media, produtos))

    resultado_ordenado = sorted(resultado, key=lambda x: x[1])

    return resultado_ordenado

if __name__ == '__main__':
    conteudo = {
    "arroz": 4.99,
    "feijão": 3.49,
    "macarrão": 2.99,
    "leite": 3.29,
    "pão": 1.99
    }
    print(maiores_que_media(conteudo))