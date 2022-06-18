'''maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('digite o {}o peso '.format(p)))
    if p == 1:
        menor = peso
        maior = peso
    else:
        if peso >= maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso registrado foi {:.1f}kg \nO menor peso registrado foi {:.1f}kg'.format(maior, menor))
'''

lst=[]  #lista vazia
for c in range(1, 6):
    peso=float(input('Peso da {}ª pessoa: '.format(c)))
    lst+=[peso]   #adc os valores de peso na lista
print('')
print('O Maior peso foi:', max(lst))  #maximo valor da lista
print('O Menor peso foi:', min(lst))  #minimo valor da lista
