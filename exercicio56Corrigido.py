'''maioridade = 0
menos20 = 0
velho = 0
idadetotal = int(0)
for c in range(1, 5):
    print('Cadastro {}: '.format(c))
    nome = input('Digite o nome: ')
    idade = int(input('Digire a idade: '))
    sexo = input('Digite o sexo (M/F): ').upper()
    idadetotal = idadetotal + idade
    if idade > maioridade and sexo == 'M':
        maioridade = idade
        velho = nome
    if sexo == 'F' and idade < 20:
        menos20 = menos20 + 1
idadetotal = idadetotal/4
if velho == 0 :
    print('A media de idade do grupo é {}'.format(idadetotal))
    print('não houve homens neste grupo')
    print('tem {} mulher(es) com menos de 20 anos'.format(menos20))
else:
    print('A media de idade do grupo é {}'.format(idadetotal))
    print('o Homem mais velho é {} e sua idade é {}'.format(velho, maioridade))
    print('tem {} mulher(es) com menos de 20 anos'.format(menos20))'''

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('-----{}ªPESSOA ----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade <20:
        totmulher20 += 1
mediaidade = somaidade/4
print('A média de idade do grupo é {} anos'. format(mediaidade))
print('O Homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))
