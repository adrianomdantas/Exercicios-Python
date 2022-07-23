from random import randint
import time
jogos = []
seisnumeros = []
print(40 * '-')
print(f'{"JOGOS DA MEGASENA":^40}')
print(40 * '-')
qtdjogos = (int(input('Quantos jogos você desehja sortear? ')))
print(f'{f" SORTEANDO {qtdjogos} JOGOS ":-^40}')
qtdnum = (int(input('Quantos numeros terão os jogos? ')))
if qtdnum < 6 or qtdnum > 15:
    while True:
        print(f'não é possível fazer jogos de {qtdnum} números na megasena')
        qtdnum = (int(input('Quantos numeros terãonos jogos? ')))
        if 6 <= qtdnum <= 15:
            break

for i in range(0, qtdjogos):
    cont = 0
    while cont < qtdnum:
        n = randint(1, 60)
        if n not in seisnumeros:
            seisnumeros.append(n)
            cont += 1
    seisnumeros.sort()
    jogos.append(seisnumeros[:])
    seisnumeros.clear()
for p, a in enumerate(jogos):
    time.sleep(1)
    print(f'Jogo n° {p + 1}: {a}')
print(f'{" Boa Sorte ":=^40}')
