"""Implemente a classe Lampada. A classe Lâmpada recebe um booleano no seu construtor, 
True se a lâmpada estiver ligada, False caso esteja desligada. A classe Lampada possuí os seguintes métodos:
    liga(): muda o estado da lâmpada para ligada
    desliga(): muda o estado da lâmpada para desligada
    esta_ligada(): retorna verdadeiro se a lâmpada estiver ligada, falso caso contrário

Para testar sua classe:
    1. Ligue a Lampada
    2. Imprima: A lâmpada está ligada? True
    3. Desligue a Lampada
    4. Imprima: A lâmpada ainda está ligada? False
"""

class Lampada:
    
    def __init__(self, ligada):
        self.ligada = ligada
    
    def liga(self):
        self.ligada = True
    
    def desliga(self):
        self.ligada = False
        
    def esta_ligada(self):
        return self.ligada
        
if __name__ == '__main__':
    l = Lampada(False)
    l.liga()
    print(f'A lâmpada está ligada? {l.esta_ligada()}')
    l.desliga()
    print(f'A lâmpada ainda está ligada? {l.esta_ligada()}')