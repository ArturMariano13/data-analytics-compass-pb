def conta_vogais(texto: str) -> int:
    vogais = 'aeiou'
    
    vogais_contadas = filter(lambda char: char.lower() in vogais, texto)
    
    return len(list(vogais_contadas))

if __name__ == '__main__':
    print(conta_vogais('testando vogais'))
