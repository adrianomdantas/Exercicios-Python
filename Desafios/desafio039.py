#Para usar o ano atual
from datetime import date
anoatual = date.today().year
#print(ano)
ano = int(input('Digite o ano do seu nascimento: '))
anos = anoatual - ano
if anos == 18:
    print('Você deverá se alistar este ano')
elif anoatual - ano < 18:
    print(f'Faltam {18 - anos} anos para você se alistar')
else:
    print(f'já passou {anos - 18} anos da data que você deveria ter se alistado')