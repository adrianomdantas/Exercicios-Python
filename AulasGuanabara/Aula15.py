# usando o break
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')

# formas de escrever o format (f strings)
# nome = 'josé'
# idade = 33
# print(f'O {nome} tem {idade} anos') Python 3.6 +
# print('O {} tem {} anos.' format(nome, idade) Python 3
# print('O %s tem %d anos.' % (nome, idade)) Python  2
