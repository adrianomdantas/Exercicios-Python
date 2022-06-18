matriz = [[0,0,0],[0,0,0],[0,0,0]]
for lin in range(0, 3):
    for col in range(0, 3):
        num = int(input(f'Digite o numero na posição {lin, col}'))
        matriz [lin][col] = num
for lin in range(0, 3):
    for col in range(0, 3):
        print(f'[{matriz[lin][col]: ^5}]', end='')
    print()

