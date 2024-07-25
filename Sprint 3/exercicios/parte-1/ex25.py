"""
Crie uma classe Avião que possua os atributos modelo, velocidade_maxima, cor e capacidade. 
Defina o atributo cor de sua classe , de maneira que todas as instâncias de sua classe avião 
sejam da cor “azul”. Após isso, a partir de entradas abaixo, instancie e armazene em uma lista 
3 objetos da classe Avião. Ao final, itere pela lista imprimindo cada um dos objetos no seguinte 
formato: “O avião de modelo “x” possui uma velocidade máxima de “y”, capacidade para “z” passageiros e é 
da cor “w”. Sendo x, y, z e w cada um dos atributos da classe “Avião”.
"""

class Aviao:
    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade
        self.cor = "azul"

# Lista de aviões
avioes = []

# Criação dos objetos Aviao
a1 = Aviao('BOIENG456', 1500, 400)
a2 = Aviao('Embraer Praetor 600', 863, 14)
a3 = Aviao('Antonov An-2', 258, 12)

# Adicionando os aviões à lista
avioes.append(a1)
avioes.append(a2)
avioes.append(a3)

# Imprimindo informações sobre cada avião
for aviao in avioes:
    print(f'O avião de modelo {aviao.modelo} possui uma velocidade máxima de {aviao.velocidade_maxima} km/h, '
          f'capacidade para {aviao.capacidade} passageiros e é da cor {aviao.cor}.')
