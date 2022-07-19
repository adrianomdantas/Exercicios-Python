preco = total = 0.0
maior = 0
menor = 999999.0
while True:
    prod = input('Digite o produto: ')
    preco = float(input('Digite o preço: R$'))
    total += preco
    if preco > 1000:
        maior += 1
    if preco < menor:
        menor = preco
        nome = prod
    continuar = input('Deseja continuar [S/N]').upper()
    while True:
        if continuar not in 'NS':
            continuar = input('!!ERRO!! \nDeseja continuar [S/N]').upper()
        else:
            break
    if continuar == 'N':
        break
print(f'{20 * "="}')
print(f'Total de gasto R${total:.2f} \n{maior} produtos custaram mais de R$1000,00 \nO produto {nome} foi o mais barato')    

