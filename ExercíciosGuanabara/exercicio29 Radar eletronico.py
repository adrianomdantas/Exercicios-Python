vel = int(input('qual a velocidade do carro? '))
if vel > 80:
    print('você excedeu a velocidade em {}km, portando a multa a pagar é de R${},00'.format(vel-80,(vel-80)*7))
else:
    print('você não ultrapassou o limite da via')
