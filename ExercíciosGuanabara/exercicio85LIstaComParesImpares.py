'''Crie um programa onde o usuario possa
digitar 7 valores numericos e cadastre-os em uma lista unica
que mantenha separado os valores pares e impares
No final mostre os valores pares e impares em ordem crescente'''
total = []
par = []
impar = []
for c in range(1, 8):
    num = int(input(f'Digite {c}° numero: '))
    if num % 2 == 0:
        par.append(num)
        par.sort()
    else:
        impar.append(num)
        impar.sort()
total.append(par[:])
total.append(impar[:])
print('+-'*30)
print(f'Os numeros pares são {total[0]}')
print(f'Os numeros impares são {total[1]}')
    
