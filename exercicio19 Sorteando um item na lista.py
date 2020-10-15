import random
sorteio = 's'
while sorteio != 'n':
    aluno1 = input('primeiro aluno: ')
    aluno2 = input('segundo aluno: ')
    aluno3 = input('terceito aluno: ')
    aluno4 = input('quarto aluno: ')
    '''escolha = input('\naperte <enter> para sortear um aluno')'''
    num = random.randint(1, 4)
    if num == 1:
        print('O sorteado foi: ',aluno1)
    elif num == 2:
        print('O sorteado foi: ',aluno2)
    elif num == 3:
        print('O sorteado foi: ',aluno3)
    elif num == 4:
        print('O sorteado foi: ',aluno4)
    sorteio = input('deseja sortear outro aluno? (s/n)')
    
