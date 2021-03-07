from datetime import date
print(20 * '=')
print('Alistamento Militar')
print(20 * '=')
ano = date.today().year
nascimento = int(input('Digite seu ano de nascimeto: '))
if ano - nascimento < 18:
    print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, ano - nascimento, ano))
    print('ainda fatam {} anos para você se alistar'.format(nascimento + 18 - ano))
    print('seu ano de alistamento será em {}'.format(nascimento + 18))
elif ano - nascimento == 18:
    print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, ano - nascimento, ano))
    print('Você deve se alistar imediatamente')
else:
    print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, ano - nascimento, ano))
    print('Você já deveria ter se alistado há {} anos.'.format(ano - nascimento -18))
    print('seu alistamento foi em {}.'.format(nascimento + 18))
