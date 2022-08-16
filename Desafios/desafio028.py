from random import randint
from socket import INADDR_ALLHOSTS_GROUP
ncomput = randint(0, 5)
player = int(input('Estou pensando em um número de 0 a 5, tente adivinhar qual é: '))
if ncomput == player:
    print(f'Parabém, eu pensei exatamente no número {ncomput}')
else:
    print(f'Errou, eu pensei em {ncomput} e você digitou {player}')
    