#Contagem crescente
for c in range(1, 11,):
    print(f'{c}', end='-')
print('fim')

#contagem decrescente
for c in range(10, 0, -1):
    print(f'{c}', end='-')
print('fim')

#Contagem crescente pulando de 2 em 2
for c in range(1, 11, 2):
    print(f'{c}', end='-')
print('fim')

#Contagem crescente com variaveis
i = int(input('Digite o inicio: '))
f = int(input('Digite o termino da contagem: '))
p = int(input('Digite os saltos'))
for c in range(i, f+1, p):
    print(f'{c}', end='-')
print('fim')

#solicitando entrada teclado varias vezes e somando todos
s = 0
for c in range(1, 5):
    d = int(input('Digite um número:'))
    s += c
print(f'O resultado foi {s}')