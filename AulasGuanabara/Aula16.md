[Anterior](Aula15.md) | [Menu Principal](/README.md/) | [Próximo](Aula17.md)  

# Tuplas  

Tuplas são variaveis cpmpostas identificadas por **()**, ou seja, que armazena mais de um valor, em Python temos 3 tipos de variaveis cmpostas, Além de Tuplas, tem Listas e Dicionários.  
As variaveis compostas tem indices para poderrmos acessar o valor que desejamos.  
exemplo:
Vamos chamar a variavel composta de lanche  

**lanche**  
|0|1|2|3|
|-|-|-|-|
|Hamburguer|Suco|Pizza|Pudim|  

No python, uma string já é uma variável composta, então, a maneira de tratar uma variável composta é muito parecido ocm a forma de tratar fatiamento de string.  
Para acessarmos um valor da tupla, usamos este eexemplo:  

```
print(lanche[2])
Pizza
```
Podemos acessar uma parte da variavel  
```
print(lanche[0:2])
('Hamburguer', 'Suco')
```
Lembrando que o Python no caso de [0:2] vai ignorar o 2 e vai mostrar apenas a posição 0 e 1.  
outro exemplo:  
```
print(lanche[1:])
('Suco', 'Pizza', 'Pudin')
```
Uma caracteristica interessante, é para ver o ultimo valor não importando o tamanho da variavel.  
```
print(lanche[-1])
Pudin
```
O -2 tras o penultimo elemento o -3 o antipenultimo e assim por diante.  
Para saber qual é o tamanho desta variável, usamos o comando **len**  
```
print(len(lanche))
4
```
Para saber os ultimos 3 elementtos da Tupla por exemplo
```
print(lanche[-3:])
Suco
Pizza
Pudin
```

E claro, podemor usar as estruturas de repetição para correr toda a variavel  
```
for c in lanche:
    print(c)

Hamburguer
Suco
Pizza
Pudin
```

Outra forma de obter o mesmo resultado do exemplo anterior  
```
for i in range(0,len(lanche)):
    print(lanche[i]) 

Hamburguer
Suco
Pizza
Pudin
```
Desta forma podemos além de exibir os elementos, podemos também exibir a posição dos elementos, mas temos outra forma de mostar a posição dos elemntos usando o **enumerate**
```
for posicao, comida in enumerate(lanche):
    print(f'{comida} na posição {posicao}')

Hamburguer na posição 0
Suco na posição 1
Pizza na posição 2
Pudin na posição 3
```
Outra forma de mostrar os itens de um Tupla, é mostra-los em ordem alfabética usando o **sorted**
```
print(sorted(lanche))
['Hamburguer', 'Pizza', 'Pudin', 'Suco']
```
Perceba que agora o python mudou os **()** para **[]**, ou seja, para fazer esta "alteração", foi necessário usar listas, mas o sorted não alterou a tupla, apenas mostrou em ordem.  

E Se usarmos a soma de Tuplas? 
```
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)

(2, 5, 4, 5, 8, 1, 2)
```
Como podemos perceber, não é uma soma de posições, e sim uma junção, logo a ordem da "soma" faz a diferença, não é possível usar o sinal de subtração para tuplas.  
Você pode utilizar o count para contar um determinado item   
```
print(c.count(5))
2
```
Podemos usar o ndex também para checar a posisão de um item  
```
print(c.index(8))
4
```
Mas ele acha apenas o primero item, para ver a segunta ocorrencia do item  
```
print(c.index(5 , 2))
3
```
Assim ele vai varrer a partis da posição 2  

Mas as Tuplas podem ser usadas com varios tipos de dados  
```
pessoa = ('Fulano', 32, 'M', 90) 
```
As Tuplas são interessante para podermos armazenar varios valores, porém, existe um aLimitação, **as Tuplas são iutáveis** isto significa que não podemos mudar um valor específico que está em uma posição em uma Tupla, nem eliminar ou adicionar um, apenas deletar a tupla inteira  
```
del(pessoas)
```
Isto serve para qualquer coisa dentro do python 



[Exemplos Aula 16](Aula16.py)