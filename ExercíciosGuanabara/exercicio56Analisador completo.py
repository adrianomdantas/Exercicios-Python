maioridade = 0
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
    print('tem {} mulher(es) com menos de 20 anos'.format(menos20))
    
