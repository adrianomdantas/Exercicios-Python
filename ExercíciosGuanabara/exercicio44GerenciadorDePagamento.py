print('{:=^40}'.format(' LOJAS DANTAS '))
preco = float(input('Qual o preço do produto? R$'))
pagamento = int(input('escolha a forma de pagamento:\n1 - a vista\n2 - a vista no cartão\n3 - 2x no cartão\n4 - 3x no cartão\nopção:_'))
if pagamento == 1:
    print('a vista, 10% de desconto, total a pagar R${:.2f}'.format(preco - preco*0.1))
elif pagamento == 2:
    print('a vista no cartão, 5% de desconto, total a pagar R${:.2f}'.format(preco - preco*0.05))
elif pagamento == 3:
    print('2x no cartão, preço normal sem juros R${:.2f}, parcelas de R${:.2f}'.format(preco, preco/2))
elif pagamento == 4:
    print('3x no cartão, 20% de juros, total R${:.2f}, parcelas de R${:.2f}'.format(preco+preco*0.2,(preco+preco*0.2)/3 ))
else:
    print('opção invalida de pagamento')
