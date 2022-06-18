dia = int(input('Quantos dias alugados? '))
km = int(input('Quantos KM rodados? '))
vdia = dia*60
vkm = km*0.15
print('O total a pagar é de R${:.2f}'.format(vdia+vkm))
