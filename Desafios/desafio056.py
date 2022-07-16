somaidade = 0
contmulher = 0
hvelho = 0
for i in range(1, 5):
    nome = input(f'Digite o nome da {i}° pessoa: ')
    idade = int(input(f'Digite a idade da {i}° pessoa: '))
    sexo = input(f'Digite o Sexo da {i}° pessoa [M / F]: ').upper()
    somaidade += idade
    if sexo == 'F' and idade < 20:
        contmulher +=1
    if idade > hvelho and sexo == 'M':
        hvelho = idade
        nomevelho = nome
print(f'A média de idade do grupo é {somaidade / 4:.1f} anos')
print(f'O Homem mais velho é o {nomevelho}')
print(f'São {contmulher} mulheres com menos de 20 anos')
    