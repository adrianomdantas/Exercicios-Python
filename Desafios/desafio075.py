n1 = int(input('Digite o um número: '))
n2 = int(input('Digite o outro número: '))
n3 = int(input('Digite o mais um número: '))
n4 = int(input('Digite o ultimo número: '))
tupla = (n1, n2, n3, n4)
cont = 0
print(tupla)
print(f'o 9 apareceu {tupla.count(9)} vezes')
print(f'O valor 3 apareceu na {tupla.index(3)}° posição')
for i in tupla:
    if i % 2:
        cont += 1
print(f'Os valores pares digitados foram: {cont}')