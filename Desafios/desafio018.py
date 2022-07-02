from math import sin, tan, cos , degrees, radians
num = float(input('Digite um ângulo: '))
rad = radians(num)
seno = sin(rad)
cosseno = cos(rad)
tangente =  tan(rad)
print(f'O ângulo de {num} tem o seno de {seno:.2f}')
print(f'O ângulo de {num} tem o cosseno de {cosseno:.2f}')
print(f'O ângulo de {num} tem a tangente de {tangente:.2f}')