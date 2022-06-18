ptermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da progressão: '))
cont = 1
termo = ptermo
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print (ptermo, end=' ')
        ptermo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))
