'''Crie um programa que leia nome, ano de nascimento e carteira de trabaho
e cadstre-os(com idade) em um dicionario, se por acaso a CTPS for diferente
de zero, o dicionado receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar'''
from datetime import datetime
dados = dict()
dados['nome'] = str(input('Digite seu nome: '))
anonasc = int(input('Digite o ano de nascimento: '))
dados['idade'] = datetime.now().year - anonasc
dados['ctps'] = int(input('carteira de trabalho (0 se não tiver): '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] =  float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + (dados['contratacao'] + 35) - datetime.now().year
print (dados)
