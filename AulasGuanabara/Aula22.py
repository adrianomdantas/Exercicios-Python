'''
#Usando importação de modulos inteiros

import uteis


num = (int(input('Digite um valor: ')))
fat = uteis.fatorial(num)
print(f'O Fatorial de {num} é {fat}')
print(f'O dobro de {num} é {uteis.dobro(num)}')


#Usando importação de parte do modulo

from uteis import fatorial, dobro


num = (int(input('Digite um valor: ')))
fat = fatorial(num)
print(f'O Fatorial de {num} é {fat}')
print(f'O dobro de {num} é {dobro(num)}')'''


#Usando pacotes

from Uteis import numeros

num = (int(input('Digite um valor: ')))
fat = numeros.fatorial(num)
print(f'O Fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')
