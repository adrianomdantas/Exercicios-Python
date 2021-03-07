soma = n1 = cont = 0
n1 = int(input('digite um numero: '))
while n1 != 999:
    soma = soma + n1
    cont += 1
    n1 = int(input('digite um numero: '))
print('foram digitados {} numeros'.format(cont))
print('e a soma dos numeros digitados é ', soma)

    
