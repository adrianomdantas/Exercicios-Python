from posixpath import split


def fatorial(n, show=False):
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