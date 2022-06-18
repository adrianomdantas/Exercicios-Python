#cidade = input('digite o nome da uma cidade: ')
#lista = cidade.split()
#if lista[0] == 'Santo':
#   print('A cidade de {} começa com nome de santo'.format(cidade))
#else:
#    print('a cidade de {} não começa com o nome de santo'.format(cidade))

cid = str(input('Em que ciadde você nasceu? ')).strip()
print(cid[0:5].upper() == 'SANTO')
