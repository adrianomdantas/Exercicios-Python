termo = int(input('Digite o primeiro termo da Progressão aritmética: '))
razao = int(input('Digite a razão para esta P.A: '))
for i in range(1, 11):
    print(termo, end=' -> ')
    termo += razao
print('Fim')