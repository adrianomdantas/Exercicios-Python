num = int(input('Digite um número para saber se eçe e par ou ímpar: '))
res = num % 2
if res == 0:
    print(f'O número {num} é par')
else:
    print(f'O número {num} é ímpar')