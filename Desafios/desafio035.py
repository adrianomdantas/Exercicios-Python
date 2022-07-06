reta1 = int(input('Digite a primeira reta: '))
reta2 = int(input('Digite a segunda  reta: '))
reta3 = int(input('Digite a terceira reta: '))
if reta1 + reta2 <= reta3 or reta2 + reta3 <= reta1 or reta3 + reta1 <= reta2:
    print('estas retas não formam um triangulo!')
else:
    print('estas retas formam um triangulo!')