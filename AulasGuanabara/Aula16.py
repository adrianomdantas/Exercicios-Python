lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudin'
print(lanche)
print(lanche[2])
print(lanche[0:2])
print(lanche[1:])
print(lanche[-1])
print(len(lanche))
for c in lanche:
    print(c)
for i in range(0,len(lanche)):
    print(lanche[i])

for posicao, comida in enumerate(lanche):
    print(f'{comida} na posição {posicao}')

print(sorted(lanche))
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.count(5))
print(c.index(8))