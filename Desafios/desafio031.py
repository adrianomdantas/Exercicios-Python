dist = int(input('Qual a distância da viagem em km: '))
if dist > 200:
    print(f'O preço da viagem será R${0.45 * dist:.2f}, R$0,45 por km')
else:
    print(f'O preço da viagem será R${0.50 * dist:.2f}, R$0,50 por km')