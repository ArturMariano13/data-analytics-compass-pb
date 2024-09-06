def process_file(file_path):
    with open(file_path, 'r') as file:
        numeros = list(map(int, file.readlines()))

    pares = list(filter(lambda x: x % 2 == 0, numeros))
    
    top_5_pares = sorted(pares, reverse=True)[:5]
    
    soma = sum(top_5_pares)
    
    print(top_5_pares)
    print(soma)

if __name__ == '__main__':
    process_file('number.txt')
