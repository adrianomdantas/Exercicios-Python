sal = float(input('Digite o seu salário: '))
limite = 1250
if sal > limite:
    print(f'Seu novo salário com reajuste de 10% será R${sal * 1.1:.2f}')
else:
    print(f'Seu salário com reajuste de 15% será R${sal * 1.15:.2f}')