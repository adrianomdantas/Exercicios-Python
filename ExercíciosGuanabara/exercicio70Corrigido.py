total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'NS':
        resp = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total de compras foi {total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {barato} que custa {menor:.2f}')

'''total = custam_mais = mais_barato = 0
cont = 0
while True:
    cont += 1
    print(20*'=')
    print('cadastro de produtos')
    print(20*'=')
    nome = str(input('nome do produto: '))
    preco = float(input('Valor: '))
    total += preco
    if cont == 1:
        mais_barato = preco
        nome_barato = nome
    if mais_barato > preco:
        nome_barato = nome
        mais_barato = preco
    if preco > 1000:
        custam_mais += 1
    continuar = ' '
    while continuar not in 'NS':
        continuar = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'Total de gasto = R${total:.2f}')
print(f'{custam_mais} custam mais de R$1000,00')
print(f'O produto {nome_barato} é o mais barato que custou {mais_barato} reais')'''

