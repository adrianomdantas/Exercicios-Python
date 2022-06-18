import math
parar = 's'
while parar != 'n':
    ang = int(input('\ndigite um angulo: '))
    seno = math.sin(math.radians(ang))
    coseno = math.cos(math.radians(ang))
    tangente = math.tan(math.radians(ang))
    print('o seno de {0} é {1:.2f}, \no coseno de {0} é {2:.2f} \na tangente de {0} é {3:.2f}'.format (ang, seno, coseno, tangente))
    parar = input('deseja consultar outro angulo? ')
print('\nobrigado')
