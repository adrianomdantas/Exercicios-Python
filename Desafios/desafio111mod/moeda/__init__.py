def aumentar(n, a, op=False):
    if op:
        return moeda(n + (n * (a / 100)))
    else:
        return n + (n * (a / 100))

def diminuir(n, a, op=False):
    if op:
        return moeda(n - (n * (a / 100)))
    else:
        return n - (n * (a / 100))

def dobro(n, op=False):
    if op:
        return moeda(n * 2)
    else:
        return n * 2

def metade(n, op=False):
    if op:
        return moeda(n / 2)
    else:
        return n / 2

def moeda(n):
    return f' R${n:.2f}'

def resumo(a, b, c):
    print(30 * '-')
    print(f'{"RESUMO DO VALOR":^30}')
    print(30 * '-')
    print(f'{"Preço analisado:":<20}{moeda(a):<10}')
    print(f'{"Dobro do preço:":<20}{dobro(a, op=True):<10}')
    print(f'{"Metade do preço:":<20}{metade(a, op=True):<10}')
    print(f'{b:<2}%{" de aumento:":<17}{aumentar(a, b, op=True):<10}')
    print(f'{c:<2}%{" de redução:":<17}{diminuir(a, c, op=True):<10}')
    print(30 * '-')