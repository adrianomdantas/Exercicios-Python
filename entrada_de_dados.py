nome = input('digite seu nome: ')
idade = int(input('digite sua idade: '))
if idade<18:
    print(nome, ', você tem ', idade,  'anos' ,'portanto você é menor de idade')
else:
    print(nome, ', você tem ', idade,  'anos' ,'portanto você é maior de idade')
