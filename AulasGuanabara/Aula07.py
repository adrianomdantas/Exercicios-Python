print('#' * 20)
nome = input('Digite Seu nome: ')
print('Prazer em te conhecer {}!'.format(nome))
print('Prazer em te conhecer {:20}!'.format(nome))
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:^20}'.format(nome))
print('Prazer em te conhecer {:=^20}'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro Valor'))
print('A soma vale {}'.format(n1+n2))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \nO produto é {}, a divisão é {:.2f}'.format(s, m, d), end= ' ')
print('Divisão inteira {} e potência {}'.format(di, e))