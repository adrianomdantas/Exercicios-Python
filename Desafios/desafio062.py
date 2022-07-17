print('Descuma os termos de uma PA')
opcao = int(input('Digite um número: '))
razao = int(input('Digite uma razão: '))
cont = 0
parar = 'S'
while parar != 'N':
    print(f'{opcao}')
    opcao += razao
    parar = input('Deseja mostrar mais um termo? [S/N]: ').upper()
    while parar not in 'SN':
        parar = input('ERRO!!! Deseja mostrar mais um termo? [S/N]: ').upper()
print('FIM')