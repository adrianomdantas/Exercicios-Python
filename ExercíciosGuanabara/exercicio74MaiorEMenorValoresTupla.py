from random import randint
a = randint(1, 10)
b = randint(1, 10)
c = randint(1, 10)
d = randint(1, 10)
e = randint(1, 10)
lista = (a, b, c, d, e)
print('os numeros sorteados são: ', end='')
for c in range(0, len(lista)):
    print(lista[c], end=' ')
print(f'\no maior numero foi {max(lista)}')
print(f'O menor numero foi {min(lista)}')



