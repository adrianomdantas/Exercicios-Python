from math import sin, tan, cos , degrees, radians
ang = float(input('Digite um ângulo: '))
rad = radians(ang)
seno = sin(rad)
cosseno = cos(rad)
tangente =  tan(rad)
print(f'O ângulo de {ang} tem o seno de {seno:.2f}')
print(f'O ângulo de {ang} tem o cosseno de {cosseno:.2f}')
print(f'O ângulo de {ang} tem a tangente de {tangente:.2f}')