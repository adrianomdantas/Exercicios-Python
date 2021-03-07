from datetime import date
ano = int(input('Digite o ano para saber se ele é bisexto: '))
bisexto = ano%4
zero = ano%10
#ano bisexto é multiplos de 4 exceto em multiplos de 100
#que não são multiplos de 400 
if ano == 0:
    ano = date.today().year
if ano %4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bisexto'.format(ano))
else:
    print('O ano {} não é bisexto'.format(ano))

