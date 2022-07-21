'''lista = ['Hamburguer','Suco','Pizza','Pudim']
print(lista)
lista[3] = 'picole'
print(lista)
lista.append('cookies')
print(lista)
lista.insert(0,'hotdog')
print(lista)
del lista[3]
print(lista)
lista.pop()
print(lista)
lista.pop(1)
print(lista)
lista.remove('Suco')
print(lista)
valores = list(range(4, 11))
print(valores)
valores = [6, 4, 8, 9, 3, 2, 4, 7, 5, 2]
valores.sort()
print(valores)
valores.sort(reverse=True)
print(valores)
print(len(valores))

lista = [1, 3, 4, 4, 6, 8, 8, 9, 3, 1]
print(lista)
while True:
    if 1 in lista:
        lista.remove(1)
    else:
        break
print(lista)'''

# outra forma de fazer a lista e correr uma lista 
'''valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('FIM')'''
# solicitando entrada do teclado
'''
valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('FIM')
'''
# Listas iguais ocupam a mesma memoria
a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista a {a}')
print(f'lista b {b}')

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista a {a}')
print(f'lista b {b}')