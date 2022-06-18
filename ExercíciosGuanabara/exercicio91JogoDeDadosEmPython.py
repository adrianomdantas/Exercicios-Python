'''Crie um programa onde 4 jogadores joguem um dado
e tenham resultados aleatorios. Guarde estes resultados
em um dicionario. No final, coloque este dicionario em ordem.
Sabendo que o Vencedor tirou o maior numero no dado'''
from random import randint
from time import sleep
from operator import itemgetter
jogadores = {}
ranking = []
for a in range(1, 5):
    dado = randint(1, 6)
    jogadores[f'jogador {a}'] = dado
for a, b in jogadores.items():
    print(f'{a} tirou {b}')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('== Ranking ==')
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar {v[0]} com {v[1]}')
    sleep(1)


    

    

