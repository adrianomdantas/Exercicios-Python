from datetime import date
nascimento = int(input('qual o ano do seu nascimento: '))
anoatual = date.today().year
idade = anoatual - nascimento
if idade <= 9:
    print('VocÊ tem {} anos, sua categoria é Mirim'.format(idade))
elif idade <= 14 and idade > 9:
    print('Você tem {} anos, sua categoria é Infantil'.format(idade))
elif idade > 14 and idade < 20:
    print('Você tem {} anos, sua categoria é Junior'.format(idade))
elif idade == 20:
    print('Você tem {} anos, sua categoria é Senior'.format(idade))
else:
    print('Você tem {} anos, sua categoria é Master'.format(idade))
