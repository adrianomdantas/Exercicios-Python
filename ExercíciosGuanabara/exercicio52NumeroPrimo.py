num = int(input('Digite um numero para saber se ele é um numero primo: '))
primo = 0
for n in range(num , 0, -1):
    if num % n == 0:
        primo += 1
if primo == 2:
    print('O numero {} é primo'.format(num))
else:
    print('O numero {} não é primo'.format(num))

    

