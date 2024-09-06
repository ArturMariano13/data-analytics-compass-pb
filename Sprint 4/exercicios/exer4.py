def calcular_valor_maximo(operadores, operandos) -> float:
    operacoes = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '%': lambda x, y: x % y
    }
    
    def aplicar_operacao(op_ope):
        operador, (x, y) = op_ope
        return operacoes[operador](x, y)
    
    return max(map(aplicar_operacao, zip(operadores, operandos)))

if __name__ == '__main__':
    operadores = ['+', '-', '*', '/', '+']
    operandos = [(3, 6), (-7, 4.9), (8, -8), (10, 2), (8, 4)]

    print(calcular_valor_maximo(operadores, operandos))