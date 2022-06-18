'''numero = ('Zero', 'um', 'Dois', 'tres', 'quatro',
'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
'onze', 'doze', 'treze', 'quatorze', 'quinze',
'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um numero de 0 a 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente: ', end='')
print(f'Você digitou o numero {numero[num]}')'''

numero = ('Zero', 'um', 'Dois', 'tres', 'quatro', 'cinco',
          'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
          'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
          'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        num = int(input('Digite um numero de 0 a 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente: ', end='')
    print(f'Você digitou o numero {numero[num]}')
    continuar = str(input('Deseja Continuar [s/n]? ')).upper().strip()[0]
    if continuar in 'SN':
        if continuar == 'S':
            print('Vamos escolher outro numero')
        if continuar == 'N':
            break
    else:
        print('Opção errada')
        continuar = str(input('Deseja Continuar? [s/n] ')).upper().strip()[0]
        if continuar == 'N':
            break
print('FIM')
