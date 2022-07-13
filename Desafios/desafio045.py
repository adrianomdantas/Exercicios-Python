from random import randint
comp = randint(1, 3)
print ('----Escolha uma opção----')
print('[ 1 ] pedra')
print('[ 2 ] papel')
print('[ 3 ] tesoura')
opcao = int(input('Digite sua opção: '))
if opcao < 1 or  opcao > 3:
    print('opção errada')
else:
    if opcao == comp:
        print('Empatamos')   
    elif comp == 1:
        if opcao == 2:
            print('Escolhi pedra, você escolheu papel, Parabens')
        else:
            print('Escolhi pedra, você escolheu tesoura, Eu ganhei')
    elif comp == 2:
        if opcao == 3:
            print('Escolhi papel, você escolheu tesoura, Parabens você ganhou')
        else:
            print('Escolhi papel, você escolheu pedra, Eu ganhei')
    elif comp == 3:
        if opcao == 1:
            print('Escolhi tesoura, você escolheu pedra, Parabéns, você ganhou')
        else:
            print('Escolhi tesoura, você escolheu papel, Eu ganhei')
            