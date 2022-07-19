#R$50, R$20, R$10, e R$1.
valor = int(input('Qual valor você quer sacar? R$'))
while True:
    if valor >= 50:
        print(f'{valor // 50} notas de R$50,00')
        valor = valor % 50
    elif 20 <= valor < 50:
        print(f'{valor // 20} notas de R$20,00')
        valor = valor % 20
    elif 10 <= valor < 20:
        print(f'{valor // 10} notas de R$10,00')
        valor = valor % 10
    elif 1<= valor < 10:
        print(f'{valor} notas de R$1,00')
        valor = 0
    else:
        break
print('Volte sempre')