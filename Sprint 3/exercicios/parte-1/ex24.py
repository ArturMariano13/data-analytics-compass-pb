"""
Crie uma classe Ordenadora que contenha um atributo listaBaguncada e que contenha os métodos
 ordenacaoCrescente e ordenacaoDecrescente.
Instancie um objeto chamado crescente dessa classe Ordenadora que tenha como listaBaguncada a
 lista [3,4,2,1,5] e instancie um outro objeto, decrescente dessa mesma classe com uma outra listaBaguncada 
 sendo [9,7,6,8].
Para o primeiro objeto citado, use o método ordenacaoCrescente e para o segundo objeto, use o método 
ordenacaoDecrescente.
"""

class Ordenadora:
    listaBaguncada = []
    def __init__(self, listaBaguncada):
        self.listaBaguncada = listaBaguncada
    
    def ordenacaoCrescente(self):
        return sorted(self.listaBaguncada)
    
    def ordenacaoDecrescente(self):
        return sorted(self.listaBaguncada, reverse=True)

lista1 = [3,4,2,1,5]
lista2 = [9,7,6,8]

crescente = Ordenadora(lista1)
decrescente = Ordenadora(lista2)

lista1 = crescente.ordenacaoCrescente()
lista2 = decrescente.ordenacaoDecrescente()

print(lista1)
print(lista2)