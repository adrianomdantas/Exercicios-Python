total = [[],[]]
for i in range(1, 8):
    tot = int(input(f'Digite o {i}° valor: '))
    if tot % 2 == 0:
        total[0].append(tot)
    else:
        total[1].append(tot)
total[0].sort()
total[1].sort()
print(f'Os números pares foram: {total[0]}')
print(f'Os valores impares foram: {total[1]}')