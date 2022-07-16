#Exemplo 1 com for
'''for c in range(1, 10):
    print(c, end='-')
print('fim')'''

#O mesmo com while
'''c = 1
while c < 10:
    print(c, end='-')
    c += 1
print('fim')'''

#Solicitando numeros indeterminadamente até que seja decidido parar
'''n = 1
while n != 0:
    n = int(input('Digite um número ou "0" para interromper: '))
print('FIM')'''

#Perguntand se o usuário quer continuar
r = 'S'
while r == 'S':
    n = int(input('Digite um número: '))
    r = input('Quer continuar? [s/n]: ').upper()
print('FIM')    
