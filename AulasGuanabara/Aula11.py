from cgi import print_form


print('\033[0;30;41mOlá Mundo!\033[m ')
print('\033[4;33;42mOlá Mundo!\033[m')
print('\033[1;35;43mOlá Mundo!\033[m')
print('\033[30;42mOlá Mundo!\033[m')
print('\033[mOlá Mundo!')
print('\033[7;30mOlá Mundo!\033[m')
#Usando Dicionário 
cores = {'limpa':'\033[m','amarelo':'\033[33m','cinza':'\033[7;30m', 'azul':'\033[34m]'}
print('Olá Mundo {} amarelo {} azul {} '.format(cores['amarelo'], cores['azul'], cores['limpa']))
#print(f'Olá mundo {cores['amarelo']} Amarelo {cores['azul']} azul {cores['limpa']}')
print(cores['azul'])
print(f'Olá mundo{cores['limpa']}')