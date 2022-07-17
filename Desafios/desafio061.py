print('Descuma os 10 primeiros termos de uma PA')
opcao = int(input('Digite um número: '))
razao = int(input('Digite uma razão: '))
cont = 0
while cont < 10:
    print(f'{opcao}', end=' -> ')
    opcao += razao
    cont += 1
print('FIM')
