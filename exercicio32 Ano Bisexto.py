ano = int(input('Digite o ano para saber se ele é bisexto: '))
bisexto = ano%4
zero = ano%100
if ano < 2020:
    if bisexto == 0 and zero != 0:
        print('Este ano foi bisexto')
    else:
        print('Este ano não foi bixesto')
else:
    if bisexto == 0 and zero != 0:
        print('Este ano será bisexto')
    else:
        print('Este ano não será bixesto')

