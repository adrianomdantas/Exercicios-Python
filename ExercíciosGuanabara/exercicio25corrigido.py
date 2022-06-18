#nome = input('Digite seu nome: ').strip()
#if nome.find('silva') >= 0:
#  print('seu nome tem silva')
#else:
#  print('seu nome nao tem silva')
nome = str(input('Digite seu nome inteiro: ')).strip()
print('Seu nome tem silva? {}'.format('silva'in nome.lower()))
