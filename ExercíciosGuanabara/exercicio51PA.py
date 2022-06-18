a1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
for n in range(1, 10):
    print(a1, end=' ')
    a1 = a1 + razao
print(a1)
