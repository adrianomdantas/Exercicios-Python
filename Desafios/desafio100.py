def sorteia(lst):
    from random import randint
    import time
    print(f'Sorteando 5 valores... ', end =' ')
    for j in range(0, 5):
        lst.append(randint(1, 10))
    for i in lst:
        time.sleep(0.5)
        print(i, end=' ', flush=True)
    print('PRONTO!')

def somaPar(lsta):
    par = 0
    for j in lsta:
        if j % 2 == 0:
            par += j
    print(f'Somando os valores pares de {lsta} temos, {par}')        


numeros = []

sorteia(numeros)
somaPar(numeros)
