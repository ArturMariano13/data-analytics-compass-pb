from functools import reduce

def calcula_saldo(lancamentos) -> float:
    def transformar_lancamento(lancamento):
        valor, tipo = lancamento
        return valor if tipo == 'C' else -valor

    valores_transformados = list(map(transformar_lancamento, lancamentos))
    
    saldo = reduce(lambda acc, x: acc + x, valores_transformados, 0)
    
    return saldo

if __name__ == '__main__':
    lancamentos = [
        (10, 'D'),
        (300, 'C'),
        (20, 'C'),
        (80, 'D'),
        (300, 'D')
    ]
    print(calcula_saldo(lancamentos))
