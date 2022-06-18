c = homem = maior = menor = 0
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
print(f'{maior} pessoas com mais de 18 anos\n{homem} homens cadastrados\n{menor} Mulheres com menos de 20 anos')
        
    

