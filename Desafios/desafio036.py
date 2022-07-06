vl_casa = float(input('Digite o valor da casa: R$'))
sal = float(input('Digite seu salário: R$'))
anos = int(input('Digite em quantos anos pretende pagar: '))
prest = vl_casa / (anos * 12)
if prest <= sal * 0.3:
    print(f'A prestação será R${prest:.2f}, e seu credito será aprovado')
else:
    print(f'Desculpe, seu crédito não sera aprovado, a prestação de R${prest:.2f} ultrapassou 30% do seu salário')