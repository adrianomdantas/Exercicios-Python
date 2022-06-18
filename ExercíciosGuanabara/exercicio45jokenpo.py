from random import randint
print('Suas Opções:\n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA')
jogo = int(input('Qual é a sua jogada? '))
pc = randint(0, 2)
if pc == 0 and jogo == 2 or pc == 1 and jogo == 0 or pc == 2 and jogo == 1:
    print('Compoutador venceu, ')
    if pc == 0 and jogo == 2:
        print('Você escolheu TESOURA \nO Computador escolheu PEDRA')
    elif pc == 1 and jogo == 0:
        print('Você escolheu PEDRA \nO Computador escolheu PAPEL')
    elif pc == 2 and jogo == 1:
        print('Você escolheu PAPEL \nO Computador escolheu TESOURA')
elif jogo == 0 and pc == 2 or jogo == 1 and pc == 0 or jogo == 2 and pc == 1:
    print('Jogador venceu, ')
    if jogo == 0 and pc == 2:
        print('O Computador escolheu TESOURA \nVocê escolheu PEDRA')
    elif jogo == 1 and pc == 0:
        print('O Computador escolheu PEDRA \nVocê escolheu PAPEL')
    elif jogo == 2 and pc == 1:
        print('O Computador escolheu PAPEL \nVocê escolheu TESOURA')
elif jogo > 2:
    print('opção errada')
else:
    print('EMPATOU')
    
