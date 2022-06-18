'''Crie um prograga que leia NOME e PESO de varias pessoas,
guardando tudo em uma LISTA. No final, mostra:
A) Quantas pessoas foram cadastradas
B)Uma lista com as pessoas mais velhas
C) Uma Lista com as pessoas mais pesadas'''

dados = list()
galera = list()
while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(float(input('Digite o peso: ')))
    galera.append(dados[:])
    dados.clear()
    fim = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while fim not in 'NS':
        fim = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if fim == 'N':
            break
    if fim == 'N':
        break
print('=-' *30)
print('{: <30}'.format('nome'), end='')
print('{: >7}'.format('peso'))
for c in range(0, len(galera)):
    for p in range(0, 2):
        print(f'{galera[c][p]}', end=' ')
        
    print('')
print(f'foram cadastradas {len(galera)} pessoas')
    
