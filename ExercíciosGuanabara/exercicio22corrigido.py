nome = str(input('digite seu nome compelo: ')).strip()#para eliminar espaços antes e depois
print('seu nome em maiuscula é', nome.upper())
print('seu nome em minuscula é', nome.lower())
print('Seu nome tem {} letras'.format(len(nome)-nome.count(' ')))#o nome inteiro menos os espaços
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))#encontra a posição do primeiro espaço
separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))
