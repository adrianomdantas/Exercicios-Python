[Anterior](Aula17.md) | [Menu Principal](/README.md/) | [Próximo](Aula19.md)  

# Listas (Parte 2)  

Podemos declarar listas dentro de listas, por exemplo:  
```
dados = ['Pedro',25]
pessoa = []
pessoas.append(dados[:])
print(pessoas)
[['Pedro', 25]]
```
Perceba que existe uma lista dentro de outra, para ficar mais claro vamos colocar mais dados dentro desta lista  
```
dados = ['Maria',19]
pessoas.append(dados[:])
dados = ['João',32]
pessoas.append(dados[:])
pessoas.append(dado)
[['Pedro', 25],['Maria', 19],['João', 32]]
```
Agora ficou bem clado que temos uma lista em cada uma das 3 posições de uma lista princial  
**OBS**  
Assim como nas tuplas, se a copia for feita apenas usando o **lista1 = lista2"** quando você mexer em uma lista, automaticamente estará mexendo na segunda lista devido as informações ficarem alocadas no mesmo lugar na memória, então usamos o **[:]** para realemente copiar o conteudo e não apenas usar a mesma posição na memória.  

Tando a posição da lista que principal quando da que está dendro pra principal continuam a mesma  
ex:  
|0|1|2|
|-|-|-|
|'Pedro', 25|'Maria', 19|'João', 32| 

Podemos declarar esta lista gigante de uma vez só:  

´´´
Pessoas = [['Pedro', 25],['Maria', 19],['João', 32]]
´´´

Consultando listas dentro de listas  
```
print(pessoas[0][0])
Pedro
```
O primeiro [0] estamos indicando a posição 0 das lista principal e o segundo [0] estamos indicando a posição 0 da lista 'secindária que está na posição 0.

Outro exemplo:  
```
Pessoas = [['Pedro', 25],['Maria', 19],['João', 32]]
print(pessoas[2][1])
32
```
E se não usarmos as duas indicações, o Python vai mostrar tudo que tem na posição:  
```
Pessoas = [['Pedro', 25],['Maria', 19],['João', 32]]
print(pessoas[1])
['Maria', 19]
```
Criando uma lista com dados do teclado
```
gal = list()
dad = list()
for i in range(0, 3):
    dad.append(input('Nome: '))
    dad.append(input('Idade: '))
    gal.append(dad[:])
    dad.clear()
print(gal)

Nome: João
Idade: 32
Nome: Maria
Idade: 55
Nome: Daniel
Idade: 33
[['João', '32'], ['Maria', '55'], ['Daniel', '33']]
```
Exemplo de mostrar quem é maior de idade e menos de idade
```
for i in gal:
    if i[1] > 18:
        print(f'{i[0]} é maior de idade')
    else:
        print(f'{i[0]} é menor de idade')

Nome: João
Idade: 33
Nome: Ana
Idade: 11
Nome: Maria
Idade: 45

João é maior de idade
Ana é menor de idade
Maria é maior de idade
```


[Exemplos Aula 18](Aula18.py)