numeros = []
par = []
impar = []
while True:
    n = (int(input('Digite um numero: ')))
    numeros.append(n)
    if n % 2 == 0:
         par.append(n)
    else:
        impar.append(n)
    resp = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Tente novamente, Deseja continuar [S/N]: ')).strip().upper()[0]
        if resp == 'N':
            break
    if resp == 'N':
        break
print('=-' * 30)    
print('Os nomeros digtados foram: ', numeros)
par.sort()
print(f'Numeros pares {par}')
impar.sort()
print(f'Nomeros impares {impar}')
