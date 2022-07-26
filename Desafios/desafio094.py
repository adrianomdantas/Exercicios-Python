pessoa = dict()
pessoas = []
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = (str(input('Sexo [MF]: '))).upper()
    while True:
        if pessoa['sexo'] not in "MF":
            pessoa['sexo'] = (str(input('Invalido, Digite Sexo [MF]: '))).upper()
        else:
            break
    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa.copy())
    opcao = str(input('Deseja cadastrar outra pessoa? [S/N]:')).upper()
    while True:
        if opcao not in 'SN':
            opcao = str(input('!ERRO! \nDeseja cadastrar outra pessoa? [S/N]: ')).upper()
            if opcao == 'N':
                break
        else:
            break
    if opcao == 'N':
        break
print(20 * '=-')
print(f'A) foram cadastradas {len(pessoas)} pessoas')
somaidade = 0
for i in pessoas:
    somaidade += i['idade']
print(f'B) A média de idade é de {somaidade/len(pessoas):.2f} anos')
print('C) A mulheres cadastradas foram ', end=' ')
for i in pessoas:
    if i['sexo'] == 'F':
        print(f'{i["nome"]}', end=' ')
print('\nD) Lista de pessoas com idade acima da média: ')
for i in pessoas:
    if i['idade'] > somaidade / len(pessoas):
        print(end='    ') 
        for k, v in i.items():
            print(f'{k}={v}; ', end='')
        print()    
print('<< ENCERRADO >>')

