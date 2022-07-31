def leiaint(tex):
    while True:
        f = input(tex)
        if len(f) == 0:
            print('\033[0;30;41mErro, digite um numeto intiero: \033[m ')
        else:
            if f.lower()[0] in ' abcdefghijklmnopqrstuvwxyz!@#$%¨&*':
                print('\033[0;30;41mErro, digite um numeto intiero: \033[m ')
            else:
                i = int(f)
                
                break
    return i
    


n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}')
