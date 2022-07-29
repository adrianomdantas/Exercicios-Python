def contador(a, b, c):
    import time
    if c < 0:
        c *= -1
    elif c == 0:
         c += 1
    if a < b:
        print(f'contagen de {a} até {b} de {c} em {c}')
        for i in range(a, b + 1, c):
            print(i, end=' ', flush=True)
            time.sleep(0.5)
        print('FIM!') 
    else:     
        print(f'contagen de {a} até {b} de {c} em {c}')
        for i in range(a, b - 1, -c):
            print(i, end=' ', flush=True)
            time.sleep(0.5)
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vês de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(ini, fim, passo)

