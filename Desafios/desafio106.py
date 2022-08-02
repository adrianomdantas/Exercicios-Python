def titulo(msn):
    print((len(msn) + 4) * '~' )
    print(f'  {msn}  ')
    print((len(msn) + 4) * '~', end='')
    

def ajuda(ajda):
    print('\033[0;0;40m')
    list = ['Acessando o manual do comando', ajda]
    j = ' '.join(list)
    print('\033[0;0;42m')
    titulo(j)
    print('\033[m')
    print('\033[0;0;47m')
    help(ajda)
    print('\033[m')



while True:
    print('\033[0;0;41m')
    titulo('SISTEMA DE AJUDA PyHELP')
    print('\033[m')
    opcao = input('Funão ou biblioteca > ')
    if opcao.upper() == 'FIM':
        break
    else:
        ajuda(opcao)
print('\033[0;0;47m')
titulo('FIM')
print('\033[m')
     