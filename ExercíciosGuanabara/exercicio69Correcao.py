tot18 = totH = totM20 = 0
while True:
    idade = int(input('idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp =' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0] 
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao Todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')









'''c = homem = maior = menor = 0
continuar = 's'
while continuar in 'Ss':
    c += 1
    print(20*'-')
    print(f'Cadastre a {c}° pessoa')
    print(20*'-')
    idade = int(input('idade: '))
    while True:
        sexo = str(input('Sexo [F/M]: ')).strip().upper()
        if sexo == 'F' or sexo == 'M':
            break
    if idade > 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        menor += 1
    continuar = str(input('\nDeseja continuar [S/N]')).strip()
print(f'{maior} pessoas com mais de 18 anos\n{homem} homens cadastrados\n{menor} Mulheres com menos de 20 anos')'''
        
    

