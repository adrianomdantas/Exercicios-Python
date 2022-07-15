from datetime import date
maior = 0
menor = 0
anoatual = date.today().year
for i in range(1, 8):
    nascimento = int(input(f'ano de nascimentoda {i} pessoa: '))
    if anoatual - nascimento < 18:
        menor += 1
    else:
        maior += 1
print(f'{maior} pessoas são maiores de idade')
print(f'{menor} pessoas são menores de idade')