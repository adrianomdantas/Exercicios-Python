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
matriz = [[0,0,0],[0,0,0],[0,0,0]]    
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input('Digite um valor para [{l}, {c}]: '))
print('=-'*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
        
print(matriz)

