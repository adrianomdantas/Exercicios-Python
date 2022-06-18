ptermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da progressão: '))
cont = 9
print(ptermo, end = ' ')
while cont != 0:
    while cont >= 1:
        ptermo = ptermo + razao
        print (ptermo, end=' ')
        cont -= 1
    cont = int(input('\nVocê quer ver mais quantos termos? '))
print('fim')
