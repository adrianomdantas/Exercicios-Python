'''Crie um programa onde o usuario possa
digitar 7 valores numericos e cadastre-os em uma lista unica
que mantenha separado os valores pares e impares
No final mostre os valores pares e impares em ordem crescente'''
num = [[],[]]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digirte o{c}° valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('=-'*30)
print(f'Todos os valores: {num}')
num[0].sort()
print(f'Os numeros pares são {num[0]}')
num[1].sort()
print(f'Os numeros impares são {num[1]}')

