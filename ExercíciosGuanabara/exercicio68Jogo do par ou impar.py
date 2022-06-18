from random import randint
n = soma = cont = vit =0
while True:
    c = randint(1, 10)
    c2 = int(input('Escolha um numero de 1 a 10: '))
    soma = c + c2
    #print(c, ' + ', c2,' = ', soma)
    escolha = int(input('[ 1 ] impar\n[ 2 ] par\n->'))
    if escolha > 2 or escolha < 1:
        escolha = int(input('opção errada, tente novamente \n[ 1 ] impar\n[ 2 ] par\n->'))
    if escolha == 1:
        if soma % 2 == 0:
            print(f'O computador escolheu {c} e deu {soma} (par), Você perdeu')
            print(f'Você ganhou {vit} vez(es)')
            break
        else:
            print(f'O Compitador escolheu {c} e deu {soma} (impar), Você ganhou')
            vit += 1    
    if escolha == 2:
        if soma % 2 == 0:
            print(f'O Computador escolheu {c} e deu {soma} (par), Você Ganhou')
            vit += 1 
        else:
            print(f'O Coputador escolheu {c} e deu {soma} (impar), Você perdeu')
            print(f'Você ganhou {vit} vez(es)')
            break
       
    
    
