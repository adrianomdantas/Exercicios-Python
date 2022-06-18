'''Crie um programa que crie uma matriz
de dimensão 3x3 e preencha com valores
lidos pelo teclado
   ________
  |  |  |  |
  |__|__|__|
  |  |  |  |
  |__|__|__|
  |  |  |  |
  |__|__|__|

No final mostre a matriz na tela
com a formação Corretan'''
valor = []
matriz = []    
for c in range(0, 3):
    for p in range(0, 3):
        valor.append(int(input(f'Digite um valor para a posição [{c},{p}]: ')))
        matriz.append(valor[:])
        valor.clear()
print('=-' * 20)
for c in range(0, 3):
    print(matriz[c], end='')
print('')
for c in range(3, 6):
    print(matriz[c], end ='')
print('')
for c in range(6, 9):
    print(matriz[c], end='')

