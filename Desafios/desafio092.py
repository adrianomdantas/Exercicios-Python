from datetime import date
anoatual = date.today().year

pessoa = {}
pessoa['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
pessoa['idade'] = anoatual - nasc
pessoa['ctps'] = int(input('Carteira d trabalho (0 não tem): '))
if pessoa['ctps'] > 0:
    pessoa['contratação'] = int(input("ano de contratação: "))
    pessoa['salario'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = (pessoa["contratação"] - nasc) + 35
    #considerando 35 anos de contribuição para aposentadoria
print(20 * "=-")
print(pessoa)
for k, v in pessoa.items():
    print(f'O {k} tem valor {v}')
