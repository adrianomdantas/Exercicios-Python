lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um numero: ')))
    opcao = (input('Deseja continuar? [S/N] ')).strip().upper()
    while True:
        if opcao not in 'NS':
            opcao = (input('!ERRO! \nDeseja continuar? [S/N] ')).strip().upper()
        else:
            break
    if opcao == 'N':
        break
for n in lista:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print(f'A lista completa é {lista}')
print(f'A lista com os pares {par}')
print(f'A lista com os impares {impar}')