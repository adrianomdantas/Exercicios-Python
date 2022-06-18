temp = list()
princ = list()
mai = men = 0
while True:
    temp.append(str(input('Digite o nome: ')))
    temp.append(float(input('Digite o peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
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
for c in range(0, len(princ)):
    for p in range(0, 2):
        print(f'{princ[c][p]}', end=' ')
        
    print('')
print(f'foram cadastradas {len(princ)} pessoas')
print(f'O maior foi {mai}kg peso de ', end='' )
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
print(f'\nO menor foi {men}kg peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]', end='')
