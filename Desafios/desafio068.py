from random import randint
cont = 0
print(f"{13 * '=-'}")
print('VAMOS JOGAR PAR OU IMPAR')
print(f"{13 * '=-'}")
while True:
    comp = randint(1, 10)
    player = int(input('Digite um numero: '))
    parimpar = input('Escolha, [P]par ou [I]Impar}').upper()
    while True:
        if parimpar not in 'PI':
            parimpar = input('Escolha, [P]par ou [I]Impar}').upper()
        else:
            break
    print(f"{13 * '--'}")
    if (comp + player) % 2 == 0:
        if parimpar == 'P':
            cont += 1
            print(f'Você jogou {player} e o computador jogpu {comp}, deu par')
        else:
            print(f'Você jogou {player} e o computador jogpu {comp}, deu Impar, você perdeu')
            break
    else:
        if parimpar == 'I':
            cont += 1
            print(f'Você jogou {player} e o computador jogpu {comp}, deu Impar')
        else:
            print(f'Você jogou {player} e o computador jogpu {comp}, deu Par, você perdeu')
            break
print(f'Você ganhou {cont} vezes ')    
