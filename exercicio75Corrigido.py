#a contaro os numeros 9
#b posição numero 3
#c quais numeros pares
num = (int(input('1° numero: ')),
         int(input('2° numero: ')),
         int(input('3° numero: ')),
         int(input('4° numero: ')))
print(f'Você digitou os valores {num}')
print(f'O numero 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1} posição')
else:
    print('O valor 3 não foi digitado')
print('Os numeros pares são: ', end=' ')
for n in num:
    if n % 2 == 0:
        print(n,end=' ')

        


