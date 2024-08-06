import hashlib

def mask_data(text):
    """Gera o hash SHA-1 de uma string e retorna o valor hexadecimal."""
    sha1 = hashlib.sha1()
    sha1.update(text.encode('utf-8'))
    return sha1.hexdigest()

def main():
    """Função principal para interagir com o usuário e gerar hashes"""
    while True:
        text = input("Digite uma string para gerar o hash SHA-1 (ou 'sair' para encerrar): ")
        if text.lower() == 'sair':
            print("Saindo...")
            break
        result_hash = mask_data(text)
        print(f"Hash SHA-1: {result_hash}")

if __name__ == "__main__":
    main()
