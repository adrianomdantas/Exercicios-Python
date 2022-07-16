maior = 0
menor = 1000
for i in range(1, 6):
    peso = float(input(f'Digite o peso da {i}° pessoa: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor5 = peso
print(f'O maior peso registrado foi {maior}kg')
print(f'O menor peso registrado foi {menor}kg')
