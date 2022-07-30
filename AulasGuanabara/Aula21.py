#help()
#print(input.__doc__)
'''
def contador(i, f, p):
    """
    Faz uma contagem e mostra na tela
    :param :i Inicio da contagem
    :param :f Fim da contagem
    :param :p Passo da contagem
    :return: sdem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='')
    print('FIM!')



help(contador)

def soma(a=0, b=0, c=0):
    s = a + b + c
    return s
    
r1 = soma(3, 2, 5)
r2 = soma(2, 3)
r3 = soma(6)    
'''
# usando o return
'''
def fatorial(num=1):
    f =1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O Fatorial de {n} é {fatorial(n)}')'''

def par(a):
    if 0 % 2 == 0:
        return True
    else:
        return False

num = (int(input('Digite um número: ')))
par(num)
print(par(num))