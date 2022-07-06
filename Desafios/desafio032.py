ano = int(input('Digite um ano para saber se ele é ou foi bisexto: '))
if ano % 400 == 0:
    print(f'O ano {ano} é bissexto')
elif ano % 100 == 0:
    print(f'O ano {ano} não é bissexto')
elif ano % 4 == 0:
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')

#Para usar o ano atual
#from datetime import date
#ano = date.today().year
#print(ano)