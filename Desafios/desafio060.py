num = int(input('Digite um número para ver seu fatorial: '))
fat = 1
print(f'{num}! = ', end='')
while num != 0:
    if num > 1:
        print(f'{num}', end=' x ')
        fat *= num 
        num -= 1
    else:
        print(f'{num}', end=' ')
        fat *= num 
        num -= 1
print(f'= {fat}')