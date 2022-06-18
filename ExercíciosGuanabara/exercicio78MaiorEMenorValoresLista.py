valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
print('=-' * 30)
print(f'Você digitou os valores {valores}')
print(f'O maior valos digitado foi o {max(valores)} nas posições', end=' ')
for pos, c in enumerate(valores):
    if c == max(valores):
        print(pos, end=' ')
print(f'\nO menor valor digitado foi o {min(valores)} nas posições', end=' ') 
for pos, c in enumerate(valores):
    if c == min(valores):
        print(pos, end=' ')
