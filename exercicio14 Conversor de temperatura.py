var = 's'
while var != 'n':
    temperatura = float(input('Informe a temperatura em °C: '))
    far = 9/5*temperatura+32
    print('A temperatura de {:.1f}°C corresponde a {:.1f}°F'.format(temperatura, far))
    var = input('Deseja continunar (s/n)? ')
