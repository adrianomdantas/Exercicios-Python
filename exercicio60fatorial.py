n0 = int(input('Digite o numero a ser fatorado: '))
n1 = n0
fator = n1
print(n0, end=' X ')
while n1 > 1:
    fator = fator * (n1 - 1)
    n1 = n1 - 1
    print(n1, end=' X ')
print('O fatorial de {} é {}.'.format(n0, fator))

'''n0 = int(input('Digite o numero a ser fatorado: '))
fator = n0
for c in range(n0 - 1, 0, -1):
    fator = fator * c
print(fator)'''


