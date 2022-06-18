soma = 0
for n1 in range (1, 7):
    num = int(input('Digite o {}o numero: '. format(n1)))
    if num % 2 == 0:
        soma = num + soma
print(soma)

