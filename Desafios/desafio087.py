matriz = []
linhas = []
somapar = tcoluna = 0
for i in range(0, 3):
    for j in range(0, 3):
        mat = (int(input(f'Digite um número para a posição [{i}, {j}]: ')))
        linhas.append(mat)
        if mat % 2 == 0:
            somapar += mat
        if j == 2:
            tcoluna += mat
        if i == 1:
            if j == 0:
                seglinha = mat
            else:
                if seglinha < mat:
                    seglinha = mat
    matriz.append(linhas[:])
    linhas.clear()

for a in matriz:
    for b in a:
        print(f'[{b:^3}]', end='')
    print('')
print(f'A soma dos pares é {somapar}')
print(f'A soma da terceira coluna é {tcoluna}')
print(f'O maior valor da segunda linha é {seglinha}')