"""
Crie uma classe  Calculo  que contenha um método que aceita dois parâmetros, X e Y, 
e retorne a soma dos dois. Nessa mesma classe, implemente um método de subtração, que 
aceita dois parâmetros, X e Y, e retorne a subtração dos dois (resultados negativos são permitidos).
"""

class Calculo:
    @staticmethod
    def soma(x, y):
        return x + y

    @staticmethod
    def subtracao(x, y):
        return x - y
    
x = 4
y = 5
calculo = Calculo()

print(f'Somando: {x} + {y} = {calculo.soma(x, y)}')
print(f'Subtraindo: {x} - {y} = {calculo.subtracao(x, y)}')
