from random import randint
nc = int(randint(1, 5))
nu = int(input('De 1 a 5, Qual numero o computador pensou? '))
if nc == nu:
    print('Parabens, você acertou')
else:
    print('Que pena, você não adivinhou, o numero correto seria {}'.format(nc))
