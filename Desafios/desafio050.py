somapares = 0
for i in range(1, 7):
    n1 = int(input(f'Digite o {i}° número inteiro de 6: '))
    if n1 % 2 == 0:
        somapares += n1
print(f'A soma dos números pares é {somapares}')

