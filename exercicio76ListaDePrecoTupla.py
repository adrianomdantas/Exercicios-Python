tupla = ('lapis','1.75','Borracha','2.00','Caderno','15.90','Estojo','25.00',
         'Transferidor','4.20','Compasso','9.99','Mochila','120.32',
         'Canetas','22.30','Livro','34.90')
print('-'*40)
print('{: ^40}'.format('Lista De Materiais'))
print('-'*40)
a = 0
b = 1
for c in range(0, len(tupla), 2):
    print(('{: <}'.format(tupla[a])),('{:.>40}'.format(tupla[b])))
    a += 2
    b += 2
print('-'*40)

        


