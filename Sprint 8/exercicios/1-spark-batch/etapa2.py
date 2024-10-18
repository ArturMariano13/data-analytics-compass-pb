animais = ['gato', 'cachorro', 'elefante', 'zebra', 'girafa', 'tigre', 'urso', 'cavalo', 
           'rinoceronte', 'hipopótamo', 'panda', 'leão', 'lobo', 'macaco', 'coelho', 
           'camelo', 'arara', 'dromedario', 'canguru', 'golfinho']

animais.sort()


[print(animal) for animal in animais]

with open('animais.csv', 'w') as file:
    for animal in animais:
        file.write(f'{animal}\n')

print("Arquivo 'animais.csv' criado com sucesso!")