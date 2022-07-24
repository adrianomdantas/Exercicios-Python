[Anterior](Aula18.md) | [Menu Principal](/README.md/) | [Próximo](Aula20.md)  

# Dicionários

Esta é a ultima dos 3 tipos de variáveis composta do Python.  
- Tuplas ()   
- Listas [] ou list()  
- Dicionário {} ou dict()   

Basicamente, tudo que pode ser usado em Tuplas e Listas, podem também ser usado no Dicionário, porém, com dicionários conseguimos usar indices literais e não só numéricos como nas listas e tuplas, e podemos personalizar estes indices.  
```
dados = dict()
dados = {'nome':'Pedro','idade':25}

print(dados['nome'])
Pedro
```

|nome|idade|  
|-|-|  
|'Pedro'|25|  

# Adicionando elementos  
Nos Dicionários o append não funciona, para adicionarmos elementos basta  
```
dados['sexo'] = 'M'
```
A estrutura da variavel composta ficará assim:  

|nome|idade|sexo|  
|-|-|-|  
|'Pedro'|25|'M'|  


para remover elementos, utilizamos o del  
```
del dados['idade']
```
|nome|sexo|  
|-|-|  
|'Pedro'|'M'|  

Podemos criar dicionários assimtambém  
```
folme = {'titulo':'Star Wars',
        'ano':1977,
        'diretor':'George Lucas'
        }
```
|filme|ano|diretor|  
|-|-|-|  
|'Star Wars'|1977|'MGeorge Lucas'|  

Os elementos 'titulo', 'ano' e 'diretor' são chamados de chaves (keys), podemos a qualquer momento acessar **itens**, **chaves** ou simplesmente os **valores**.  
Diferença entre Itens, chaver e valores:  
**print(filme.values())**  
'Star Wars',1977,'MGeorge Lucas'
retornou apenas os valores   
  
**print(filme.keys())**  
filme,ano,diretor
retornou apenas as chaves  
  
**print(filme.items())**  
{'titulo':'Star Wars','ano':1977,'diretor':'George Lucas'}  
retornou tanto valores como as chaves  
  
Ppodemos usar as estruturas de repetição com Dicionário e também pode juntar listas, tuplas e dicionários  por exemplo:  
|0|1|2|  
|-|-|-|  
|dicionario1|dicionario2|dicionario3|  

exemplos:  
```
pessoas = {'nome':'Adriano', 'idade':42, 'sexo':'M'}
print(pessoas)
{'nome': 'Adriano', 'idade': 42, 'sexo': 'M'}

print(pessoas.items())
dict_items([('nome', 'Adriano'), ('idade', 42), ('sexo', 'M')])

print(pessoas.keys())
dict_keys(['nome', 'idade', 'sexo'])

print(pessoas.values())
dict_values(['Adriano', 42, 'M'])

#print formatado
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
O Adriano tem 42 anos
```
Usando print formatado em um laço de repetição:  
```
for k in pessoas:
    print(k)

nome
idade
sexo


for k in pessoas.keys():
    print(k)

nome
idade
sexo


for k in pessoas.values():
    print(k)

Adriano
42
M


for k, v in pessoas.items():
    print(f'{k} = {v}')

nome = Adriano
idade = 42
sexo = M
```
Perceba que não temos o enumerate, com dicionários temos que usar o **itens**  
  
Deletando um valor  
```
del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')

nome = Adriano
idade = 42
```
Alterando um dado   
```
pessoas['nome'] = 'Fulano'
for k, v in pessoas.items():
    print(f'{k} = {v}')

nome = Fulano
idade = 42
```
Adicionando dados  
```
pessoas['peso'] = 98.8
for k, v in pessoas.items():
    print(f'{k} = {v}')

nome = Fulano
idade = 42
peso = 98.8
```
Criando um dicionário dentro de uma lista  
```
brasil = []
estado1 = {'Uf':'Rio de Janeiro','Sigla': 'RJ'}
estado2 = {'UF':'São Paulo','Sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil)
[{'Uf': 'Rio de Janeiro', 'Sigla': 'RJ'}, {'UF': 'São Paulo', 'Sigla': 'SP'}]
```
Na posição brasil[0] temos uma lista e na posição brasil[1] temos outra lista  
  
Para copiar um dicionário para dento de uma lista, não podemos usar o [:], temos que usar um metodo copy()  
exemplo:  
```
brasiltodo = []
estados = {}
for c in range(0, 3):
    estados['uf'] = str(input('Unidade Federativa: '))
    estados['sigla'] = str(input('Sigla do Estado: '))
    brasiltodo.append(estados.copy())
print(brasiltodo)

[{'uf': 'São Paulo', 'sigla': 'SP'}, {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}, {'uf': 'Minas Gerais', 'sigla': 'MG'}]
```
outro exemplo:  
```
print(brasiltodo)
for e in brasiltodo:
    for k, v in e.items():
        print(f'O campo {k} tem o valor {v}')

O campo uf tem o valor sampa
O campo sigla tem o valor sp
O campo uf tem o valor rio
O campo sigla tem o valor rj
O campo uf tem o valor minas
O campo sigla tem o valor mg
```
ou ainda outro exemplo  
```
for c in brasiltodo:
    for v in c.values():
        print(v, end=' ')
    print()

bahia BA 
Rio RJ 
Sampa SP
```


[Exemplos Aula 18](Aula18.py)