digitado = input('digite uma frase: ')
frase = digitado.upper()
#print(frase)
separado = frase.split()
#print(separado)
junto = ''.join(separado)
#print(junto)
invertido = list(reversed(junto))
#print(invertido)
invertidojunto = ''.join(invertido)
#print(invertidojunto)
if junto == invertidojunto:
    print(f'A frase "{digitado}" é um palindromo')
else:
    print(f'A frase "{digitado}" não é um palindromo')