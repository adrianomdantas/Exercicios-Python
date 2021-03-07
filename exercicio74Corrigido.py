from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('os numeros sorteados são: ', end='')
for n in numeros:
    print(f'{n}', end=' ')
print(f'\no maior numero foi {max(numeros)}')
print(f'O menor numero foi {min(numeros)}')



