"""
Implemente duas classes, Pato e Pardal , que herdam de uma superclasse chamada Passaro as 
habilidades de voar e emitir som. Contudo, tanto Pato quanto Pardal devem emitir sons diferentes (de maneira escrita) no console, 
conforme o modelo a seguir.
Imprima no console exatamente assim:
Pato
Voando...
Pato emitindo som...
Quack Quack
Pardal
Voando...
Pardal emitindo som...
Piu Piu
"""

class Passaro:
    def voar(self):
        return 'Voando...'
    
    def emitirSom(self):
        return f'{self.nome} emitindo som...\n{self.som}'

class Pato(Passaro):
    def __init__(self):
        self.nome = 'Pato'
        self.som = 'Quack Quack'

class Pardal(Passaro):
    def __init__(self):
        self.nome = 'Pardal'
        self.som = 'Piu Piu'

pato = Pato()
pardal = Pardal()

print(f'{pato.nome}\n{pato.voar()}\n{pato.emitirSom()}\n{pardal.nome}\n{pardal.emitirSom()}')