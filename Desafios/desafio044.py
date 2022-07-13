preco = float(input('digite o valor do produto: '))
print('Escolha a forma de pagamento')
print('[ 1 ] À vista Dinheiro/cheque: 10% de desconto')
print('[ 2 ] À vista no cartão: 5% de desconto')
print('[ 3 ] Em até 2x no cartão: Preço normal')
print('[ 4 ] 3x ou mais no cartão: 20% de juros')
opcao = int(input('Digite a forma de pagamento: '))
if opcao == 1:
    print(f'O valor do prodto é R${preco:.2f}, com desconto de 10% fica R${preco * 0.9:.2f}')
elif opcao == 2:
    print(f'O valor do prodto é R${preco:.2f}, com desconto de 5% fica R${preco * 0.95:.2f}')
elif opcao == 3:
    print(f'O valor do prodto é R${preco:.2f}')
elif opcao == 4:
    print(f'O valor do prodto é R${preco:.2f}, com juros de 20% fica 3 parcelas de R${(preco * 1.2)/3:.2f}')
else:
    print('Opção inválida')