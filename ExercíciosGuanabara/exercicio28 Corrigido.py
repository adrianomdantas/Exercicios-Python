from random import randint
from time import sleep
computador = int(randint(1, 5))
print('-=-' * 20)
print('Vou pensr em um numero entre 0 e 5, tente adivihar...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? '))
print('processando ...')
sleep(2)
if computador == jogador:
    print('Parabens, você acertou')
else:
    print('Que pena, você não adivinhou, o numero correto seria {}'.format(computador))
