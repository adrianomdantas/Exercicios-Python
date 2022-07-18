n = 0
cont = 0
soma = 0
while n != 999:
    n = int(input('Digite um número e 999 para sair: '))
    if n != 999:
        cont += 1
        soma += n
print(f'Foram digitados {cont} números e a soma deles é {soma}')       
        
