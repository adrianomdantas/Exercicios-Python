while True:
    print(f'\n{21 * "#"}')
    print(f'{" TABUADA ":#^21}')
    print(f'{21 * "#"}')
    tab = int(input('Digite um número para ver a sua tabuada: '))
    if tab < 0:
        break
    for i in range(1, 11):
        print(f'{tab:<3}X{i:>3}={tab * i:>3}')
        