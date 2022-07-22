'''teste = str(input("Digite a expressão matemática:"))
print(teste)
cont1 = cont2 = 0

for i in teste:
    if i == '(':
        cont1 += 1
    elif i == ')':
        cont2 += 1
if cont1 == cont2:
    print('A expressão está correta')
else:
    print('A expressão não está correta')'''
# resolvido pelo Guanabara
exp = str(input('Digite uma expressão '))
lista = []
for i in exp:
   if i == '(':
        lista.append('(')
   elif i == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão é valida')
else:
    print('Esta expressão não é válida')

