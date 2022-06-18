salario = float(input('Digite seu salatio para saber o seu aumento R$'))
if salario > 1250:
    print('Seu aumento será de R${}, portanto eu novo salário será {}'.format(salario * 0.10, salario + salario * 0.10))
else:
    print('Seu aumento será de R${}, portanto eu novo salário será {}'.format(salario * 0.15, salario + salario * 0.15))


