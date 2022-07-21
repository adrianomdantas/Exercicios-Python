valores = []
maior = 0
menor = 1000
for i in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {i}: ')))
print(20 * "=-")
print(f'Você digitou os valores{valores}')
for val in (valores):
    if val > maior:
        maior = val  
    if val < menor:
        menor = val
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for p, i in enumerate(valores):
    if i == maior:
        print(f'{p}...',end=' ')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='') 
for p, i in enumerate(valores):
    if i == menor:
        print(f'{p}...',end=' ')
print('\n')

