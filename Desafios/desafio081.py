lista = []
while True:
    lista.append(input('Digite um numero: '))
    opcao = (input('Deseja continuar? [S/N] ')).strip().upper()
    while True:
        if opcao not in 'NS':
            opcao = (input('!ERRO! \nDeseja continuar? [S/N] ')).strip().upper()
        else:
            break
    if opcao == 'N':
        break
lista.sort(reverse=True)
print(f'Ordem decrescente {lista}')
print(f'Foram digitados {len(lista)} números')
if '5' in lista:
    print('o 5 foi digitado')
else:
    print('o 5 não foi digitado')    
    


