multsom = 0
cont =0
for i in range(1, 501):
    if i % 2 != 0:
        if i % 3 == 0:
            multsom += i
            cont += 1
print(f'A soma dos {cont} números é {multsom}')