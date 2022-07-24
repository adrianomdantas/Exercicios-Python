pessoas = {'nome':'Adriano', 'idade':42, 'sexo':'M'}
print(pessoas)
print(pessoas.items())
print(pessoas.keys())
print(pessoas.values())
#print formatado
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
#print formatado em laço de repetição
for k in pessoas:
    print(k)
for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
for k, v in pessoas.items():
    print(f'{k} = {v}')
del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')
def new_func(pessoas):
    pessoas['nome'] = 'Fulano'

new_func(pessoas)
for k, v in pessoas.items():
    print(f'{k} = {v}')

pessoas['peso'] = 98.8
for k, v in pessoas.items():
    print(f'{k} = {v}')

#criando um dicionário dentro de uma lista
brasil = []
estado1 = {'Uf':'Rio de Janeiro','Sigla': 'RJ'}
estado2 = {'UF':'São Paulo','Sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)

#copyano dicionarios para dentro de listas metodo copy
brasiltodo = []
estados = {}
for c in range(0, 3):
    estados['uf'] = str(input('Unidade Federativa: '))
    estados['sigla'] = str(input('Sigla do Estado: '))
    brasiltodo.append(estados.copy())
print(brasiltodo)
for e in brasiltodo:
    for k, v in e.items():
        print(f'O campo {k} tem o valor {v}')

for c in brasiltodo:
    for v in c.values():
        print(v, end=' ')
    print()