r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))
if r1 + r2 >r3 and r2 + r3 > r1 and r3 + r1 > r2:
    if r1 == r2 == r3:
        print('sim, formam um triangulo EQUILATERO')
    elif r1 == r2 != r3 or r2 == r3 != r1 or r3 == r1 != r2:
        print('Sim, forma um triangulo ISOSCELES')
    else:# r1 != r2 != r3:
        print('Sim, forma um triangulo ESCALENO')
else:
    print('Não formam um triangulo')
   


