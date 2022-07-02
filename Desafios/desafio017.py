from math import hypot
cat1 = float(input('Digite o primeiro cateto: '))
cat2 = float(input('Digite o segundo cateto: '))
print(f'Para os catetos {cat1} e {cat2} a hipotenusa é {hypot(cat1, cat2):.2f}')