pesomaior = float(0)
pesomenor = float(500)
for c in range(1, 6):
    peso = float(input('digite o {}o peso '.format(c)))
    if peso <= pesomenor:
        pesomenor = peso
    if peso >= pesomaior:
        pesomaior = peso
print('o maior peso registrado foi {:.1f}kg e o menor peso registrado foi {:.1f}kg'.format(pesomaior, pesomenor))
