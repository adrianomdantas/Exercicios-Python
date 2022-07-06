n1 = int(input("digite o primeiro número: "))
n2 = int(input("digite o segundo  número: "))
n3 = int(input("digite o terceiro número: "))
maior = n1
menor = n1
if n2 > maior:
    maior = n2
if n2 < menor:
    menor = n2
if n3 > maior:
    maior = n3
if n3 < menor:
    menor = n3
print(f'Os numeros digitados foram {n1}, {n2}, {n3}, o maior é o {maior} e o menor é o {menor}')