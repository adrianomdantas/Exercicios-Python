'''from random import randint
comp = randint(0,10)
player = int(input('De 0 a 10, Adivinhe o numero que o computador pensou: '))
while player != comp:
    if comp > player:
        player = int(input('Mais ... Tente novamente: '))
    if comp < player:
        player = int(input('Menos ... Tente novamente: '))
print('!!!Você acertou!!! \nO computador escolheu {} e você digitou {}'.format(comp, player))'''

from random import randint
computador = randint(0, 10)
print('Sou seu computador e acabei de pensar em um numero entre 0 e 10. ')
print('Será que você consegue adivinhar  qual foi? ')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tende mais uma vez')
print('Acertou com {} palpites'. format(palpite))    
