def leiaint(tex):
    while True:
        f = input(tex)
        if len(f) == 0:
            print('\033[0;0;31mErro, digite um número intiero: \033[m ')
        elif f.lower()[0] in ' abcdefghijklmnopqrstuvwxyz!@#$%¨&*':
            print('\033[0;0;31mErro, digite um número intiero: \033[m ')
        else:
            i = int(f)
            break
    return i
    


n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}')
