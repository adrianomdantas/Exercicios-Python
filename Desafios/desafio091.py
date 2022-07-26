from operator import itemgetter
from random import randint
import time
jogadores = {}
for i in range(1, 5):
    jogadores['Jogador1'] = randint(1, 6)
    jogadores['Jogador2'] = randint(1, 6)
    jogadores['Jogador3'] = randint(1, 6)
    jogadores['Jogador4'] = randint(1, 6)

for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
    time.sleep(1)
print('RANKING DOS JOGADORES')
ranking = dict()
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
#print(ranking)
cont = 1
for i in ranking:
    print(f'O {cont}° lugar foi {i[0]} com {i[1]}')
    cont += 1
    time.sleep(1)
    
    