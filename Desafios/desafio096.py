def area(l, c):
    a = l * c
    print(f'A area do terreno {l} x {c} é {a:.2f}m2')


print('Controle de Terreno')
print(20 * '-')
larg = float(input('Largura em metros: '))
comp = float(input('Comprimento em metros: '))
area(larg, comp)
