'''sexo = str(input('Digite o  sexo [M/F]: ')).upper()[0].strip()
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Opção invalida,\nDigite novamente: ')).upper()
print('Você digitou {}.'.format(sexo))'''

sexo = str(input('Digite o  sexo [M/F]: ')).upper()[0].strip()
while sexo not in 'MmFf':
    sexo = str(input('Opção invalida,\nDigite novamente: ')).upper()
print('Você digitou {}.'.format(sexo))
