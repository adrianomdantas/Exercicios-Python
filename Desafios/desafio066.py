cont = 0
soma = 0
while True:
    n = int(input('Digite um número, e 999 para parar: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Foram digitados {cont} numeros e a soma deles é {soma}')