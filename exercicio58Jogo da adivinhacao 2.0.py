from random import randint
comp = randint(1,10)
player = int(input('De 0 a 10, Adivinhe o numero que o computador pensou: '))
while player != comp:
    player = int(input('Tente novamente: '))
print('!!!Você acertou!!! \nO computador escolheu {} e você digitou {}'.format(comp, player))
