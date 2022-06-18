'''from math import sqrt'''
from math import hypot
catop = float(input('Digite o cateto oposto do triangulo retangulo: '))
catadj = float(input('Digite o cateto adjacente do triangulo retangulo: '))
'''hip = sqrt(catop**2 + catadj**2)'''
hip = hypot(catop, catadj)
print ('o valor da hipotenusa e´ {:.2f}: '.format(hip))
