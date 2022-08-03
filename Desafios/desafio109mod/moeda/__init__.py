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