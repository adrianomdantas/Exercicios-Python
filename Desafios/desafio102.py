from posixpath import split


def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número
    :param n: O número a ser calculado
    :param show: (opcional) mostrar ou não a conta
    :return: o valor do fatorial de um numero n
    """
    tot = 1
    list = []
    for i in range(n, 0, -1):
        tot *= n
        list.append(str(n))
        n -= 1
    if show:
        juntarlista = (' x '.join(list))
        return f'{juntarlista} = {tot}'
    else:
        return tot
        

print(fatorial(10))