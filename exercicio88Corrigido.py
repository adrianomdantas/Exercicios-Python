from random import randint
lista = list()
jogos = list()
cont = 0
print('='*30)
print('joga na megasena')
print('-'*30)
quant = int(input('Quantos jogos você deseja fazer? '))
tot = 0
while tot < quant:
    cont = 0
    while True:
        num = randint(0, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
for ind, lis in enumerate(jogos):
    print(f'jogo {ind+1}', lis)
    

    

