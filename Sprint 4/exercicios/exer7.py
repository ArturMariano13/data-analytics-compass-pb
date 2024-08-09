def pares_ate(n: int):
    for i in range(2, n + 1):
        if i % 2 == 0:
            yield i

if __name__ == '__main__':
    gerador = pares_ate(20)

    for valor in gerador:
        print(valor)
