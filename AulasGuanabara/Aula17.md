[Anterior](Aula15.md) | [Menu Principal](/README.md/) | [Próximo](Aula17.md)  

# Listas (Parte 1)

Listas, são semelhantes as Tiplas com a diferença que você pode alterar, adicionar ou remover itens.  
A representação das Tuplas sao os () no caso das listas são os [].  
Para começar uma lista vazia existem 2 maneiras  
lista = []  
lista = list()  
```
lista = ['Hamburguer','Suco','Pizza','Pudim']
print(lista)
['Hamburguer', 'Suco', 'Pizza', 'Pudim']

lista[3] = 'picole'
print(lista)
['Hamburguer', 'Suco', 'Pizza', 'picole']
```
Pra adicionar itens, usamos o comando **lista.append()**
```
lista.append('cookies')
print(lista)
['Hamburguer', 'Suco', 'Pizza', 'picole', 'cookies']
```
Observe que o item é adicionado ao final da lista, para inserir um item no em qualquer parte da lista usamos o comando ***lista.insert()**  
```
lista.insert(0,'hotdog')
print(lista)
['hotdog', 'Hamburguer', 'Suco', 'Pizza', 'picole', 'cookies']
```
Observe que agora o item foi inserido na posição que a gente selecionou e os outros itens foram adequados na lista.  
E para apagar um elemento usamos o **del.lista[]**  
```
del lista[3]
print(lista)
['hotdog', 'Hamburguer', 'Suco', 'picole', 'cookies']
```
Uma outra forma de deletar é usar o **listas.pop()**, usamos para deletar o ultimo item, mas também pode ser usado para deletar qualquer posição   
```
['hotdog', 'Hamburguer', 'Suco', 'picole', 'cookies']
lista.pop()
print(lista)
['hotdog', 'Hamburguer', 'Suco', 'picole']

lista.pop(1)
print(lista)
['hotdog', 'Suco', 'picole']
```
Uma outra forma de remover um item é pelo valor **lista.remove('')**  
```
['hotdog', 'Suco', 'picole'
lista.remove('Suco')
print(lista)
['hotdog', 'picole']
```
**OBS**  
Se tiver dois itens com o mesmo nome, será removido apenas o que estiver na posição menor (primeira ocorrência) para remover todos os itens repetidos, pode ser usado um laço com uma condição
```
lista = [1, 3, 4, 4, 6, 8, 8, 9, 3, 1]
print(lista)
while True:
    if 1 in lista:
        lista.remove(1)
    else:
        break
print(lista)

[1, 3, 4, 4, 6, 8, 8, 9, 3, 1]
[3, 4, 4, 6, 8, 8, 9, 3]
```

Podemos criar uma lista usando o comando range
```
valores = list(range(4, 11))
print(valores)
[4, 5, 6, 7, 8, 9, 10]
```
Ou podemos usar o sort para organizar a lista  
```
valores = [6, 4, 8, 9, 3, 2, 4, 7, 5, 2]
valores.sort()
print(valores)
[2, 2, 3, 4, 4, 5, 6, 7, 8, 9]
```  
E pra ordem inversa podemos usar o **reverse**  
```
valores.sort(reverse=True)
print(valores)
[9, 8, 7, 6, 5, 4, 4, 3, 2, 2]
```  
Para saber o tamanho (quantos itens tem na lista) também usamos o **len**  
```
print(len(valores))
10
```
Podemos usar o **enumerate** assim como nas Tuplas  
```
valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('FIM')

Na posição 0 encontrei o valor 5
Na posição 1 encontrei o valor 9
Na posição 2 encontrei o valor 4
FIM
```
Solicitando dados do teclado   
```
valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('FIM')
```

Quando igualamos 2 listas, os itens felas ficam armazenados na mesma posição da memória, logo se alterarmos uma, alteramos a outra também   
```
a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista a {a}')
print(f'Lista b {b}')

Lista a [2, 3, 8, 7]
Lista b [2, 3, 8, 7]
```
Neste caso não estamos fazendo uma cópia e sim uma ligaçao de uma lista com a outra.  
A forma correta de copiar uma lista para outra :  
```
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista a {a}')
print(f'lista b {b}')

Lista a [2, 3, 4, 7]
lista b [2, 3, 8, 7]
```
Perceba que agora todo o conteúdo da lista a foi copiado para a lista b e quando alterado uma lista não mexemos na outra.  

[Exemplos Aula 17](Aula17.py)