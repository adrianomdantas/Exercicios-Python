n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
if n1 < n2:
    print('o numero {} é maior do que o numero {}'.format(n2, n1))
elif n2 < n1:
    print('O numero {} é maior do que o numero {}'.format(n1, n2))
else:
    print('Os numeros {} e {} são iguais'.format(n1, n2))
