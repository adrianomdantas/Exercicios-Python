def leiadinheiro(tex):
    while True:
        f = input(tex).strip().replace(",",".")
        if len(f) == 0:
            print('\033[0;0;31mErro, digite um número intiero: \033[m ')
        elif f.lower()[0] in '.,<>}{[()] abcdefghijklmnopqrstuvwxyz!@#$%¨&*':
            print('\033[0;0;31mErro, digite um número intiero: \033[m ')
        else:
            break
    return float(f)
