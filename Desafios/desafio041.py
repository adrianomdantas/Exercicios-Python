from datetime import date
anoatual = date.today().year
nascimento = int(input('Digite o ano de nascimento para saber a categoria: '))
idade = anoatual - nascimento
if idade <= 9:
    print(f'Com {idade} anos, sua categogie é Mirim')
elif 9 < idade <= 14:
    print(f'Com {idade} anos, sua categpria é Infantil')
elif 14 < idade <= 19:
    print(f'Com {idade} anos, sua categpria é Júnior')
elif idade == 20:
    print(f'Com {idade} anos, sua categpria é Sênior')
else:
    print(f'Com {idade} anos, sua categpria é Master')