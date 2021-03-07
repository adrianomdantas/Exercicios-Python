print('=' * 30)
print('{:^30}'.format('BANCO CVE'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cedulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao banco CEV! Tenha um bom dia')



'''print(15*'=')
print('BANCO DO NANO')
print(15*'=')
valor = int(input('Digite o valor a ser sacado: R$'))
divisao_inteiro50 = valor % 50
divisao_resto50 = valor // 50

divisao_inteiro20 = divisao_inteiro50 % 20
divisao_resto20 = divisao_inteiro50 // 20

divisao_inteiro10 = divisao_inteiro20 % 10
divisao_resto10 = divisao_inteiro20 // 10

divisao_inteiro1 = divisao_inteiro10 % 1
divisao_resto1 = divisao_inteiro10 // 1

if divisao_resto50 > 0:
    print(divisao_resto50, ' notas de R$50,00')
    
if divisao_resto20 > 0:
    print(divisao_resto20, ' notas de R$20,00')
    
if divisao_resto10 > 0:
    print(divisao_resto10, ' notas de R$10,00')
    
if divisao_resto1 > 0:
    print(divisao_resto1, ' notas de R$1,00')
print(15*'-')
print('Volte sempre')'''
