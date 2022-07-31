from posixpath import split


def fatorial(n, show=False):
    tot = 1
    list = []
    for i in range(n, 0, -1):
        tot *= n
        list.append(n)
        n -= 1
    if show:
        return f'{list} = {tot}'
    else:
        return tot
        

print(fatorial(5))