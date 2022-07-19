homem = mulhermenor = maior18 = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = input('Digite oSexi [F/M]: ').upper()
    while True:
        if sexo not in 'MF':
            sexo = input('Digite oSexi [F/M]: ').upper()
        else:
            break
    if idade > 18:
        maior18 += 1
    if sexo == 'M':
        homem += 1
    if idade < 20 and sexo == 'F':
        mulhermenor += 1
    parar = input('Deseja cadastrar outra pessoa? [S/N]: ').upper()
    while True:
        if parar not in 'SN':
            parar = input('!!ERRO!! Deseja cadastrar outra pessoa? [S/N]: ').upper()
        else:
            break
    if parar == 'N':
        break
print(f'{" FIM ":#^21}')
print(f'Foram cadastrados: \n{maior18} Pessos maior de 18 anos \n{homem} Homens \n{mulhermenor} mulheres menores de 20 anos')
