from random import randint
n1 = randint(1, 100)
n2 = randint(1, 100)
n3 = randint(1, 100)
n4 = randint(1, 100)
n5 = randint(1, 100)
tupla = (n1, n2, n3, n4, n5)
menor = maior = n1
print('Os números sorteados foram: ', end='')
for i in tupla:
    print(i, end=' ')
    if maior < i:
        maior = i
    if menor > i:
        menor = i
print(f'\nO menor número foi o {menor}')
print(f'O maior número foi o {maior}')
