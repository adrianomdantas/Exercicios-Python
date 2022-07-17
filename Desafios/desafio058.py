from ast import Import
from random import randint
numcomp = randint(0, 10)
cont=1
print('Vamos ver em quantas tentativas você vai acertar o numero que eu pensei de 0 a 10')
numplayer = int(input(f'{cont}° tentativa :'))
while numcomp != numplayer:
    if numcomp != numplayer:
        cont +=1
        numplayer = int(input(f'{cont}° tentativa :'))
print(f'Você acertou na {cont}° tentantiva')