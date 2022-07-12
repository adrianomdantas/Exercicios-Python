lado1 = float(input(']digite o 1° lado: '))
lado2 = float(input(']digite o 2° lado: '))
lado3 = float(input(']digite o 3° lado: '))
if lado1 + lado2 <= lado3 or lado2 + lado3 <= lado1 or lado3 + lado1 <= lado2:
    print('estas retas não formam um triangulo!')
else:
    if lado1 == lado2 == lado3:
        print('triangulo Equilátero')
    elif lado1 != lado2 != lado3:
        print('triangulo Escaleno')
    else:
        print('triangulo Isóceles')
    
