pessoa = []
galera = []
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    galera.append(pessoa[:])
    pessoa.clear()
    opcao = (str(input('Deseja cadastrar outra pessoa? [S/N]'))).strip().upper()
    while True:
        if opcao not in 'SN':
            opcao = (str(input('Deseja cadastrar outra pessoa? [S/N]'))).strip().upper()
        else:
            break
    if opcao == 'N':
        break
for a in range(0, len(galera)):
    for b in range(1 , 2, 2):
        if a == 0:
            maior = menor = galera[a][b]
        else:
            if maior < galera[a][b]:
                maior = galera[a][b]
            if menor > galera[a][b]:
                menor = galera[a][b]

print(galera)
print(f'Ao todo você cadastrou {len(galera)} pessoas')
print(f'O maior peso foi de {maior}kg. Peso de ', end=' ')
for a in range(0, len(galera)):
    for b in range(1 , 2, 2):
        if galera[a][1] == maior:
            print(f'[{galera[a][0]}]', end=' ') 

print(f'\nP menor peso foi de {menor}kg. Peso de ', end=' ')
for a in range(0, len(galera)):
    for b in range(1 , 2, 2):
        if galera[a][1] == menor:
            print(f'[{galera[a][0]}]', end=' ')
print('')