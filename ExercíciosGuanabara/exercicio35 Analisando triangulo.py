r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))
if r1 == r2 == r3:
    print('Sim, estas retas formam um triangulo')
else:
    if r1 > r2 and r1 > r3:
        if r2 + r3 > r1:
            print('Sim, estas retas formam um triangulo')
        else:
            print('Não, estas retas não formam um triangulo')
    if r2 > r3 and r2 > r1:
        if r1 + r3 > r2:
            print('Sim, estas retas formam um triangulo')
        else:
            print('Não, estas retas não formam um triangulo')
    if r3 > r2 and r3 > r1:
        if r2 + r1 > r3:
            print('Sim, estas retas formam um triangulo')
        else:
            print('Não, estas retas não formam um triangulo')


