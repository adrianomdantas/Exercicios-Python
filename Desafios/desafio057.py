sexo = str(input('Digite seu sexo [M / F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Opção errada, Digite seu sexo [M / F]: ')).upper()
print(f'Sexo {sexo} registrado com sucesso')