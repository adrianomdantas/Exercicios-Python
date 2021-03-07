numero = ('Zero', 'um', 'Dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
c = int(input('Digite um numero de 0 a 20: '))
if c < 0 or c > 20:
    while True:
        c = int(input('Tente novamente. Digite um numero de 0 a 20: '))
        if c >= 0 and c <= 20:
            break
print(f'Você digitou o numero {numero[c]}')
