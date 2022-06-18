frase = str(input('Digite uma frase:\n->')).strip()
separado = frase.split()
junto = ''.join(separado)
correto = list(junto.upper())
invertido = list(reversed(junto.upper()))
print(correto)
print(invertido)
if correto == invertido:
    print('verdadeiro')
else:
    print('falso')

