frase = str(input('Digite uma frase:\n->')).strip().upper()
separado = frase.split()
junto = ''.join(separado)
print('Você digitou a frase{} '.format(junto))
'''inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]'''
inverso = junto[::-1]
print('o inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos parindromo')
else:
    print('A frase digitada não é parindromo')
