from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou impar: ')). strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}', end='')
    print(' Deu Par' if total %2 == 0 else ' Deu Impar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu !')
            v += 1
        else:
            print('Você perdeu !')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você Venceu !')
            v += 1
        else:
            print('Você perdeu !')
            break
    print('Vamos jogar novamente ...')
print(f'GAME OVER! Você venceu {v} vezes.') 
    
