[Anterior](Aula19.md) | [Menu Principal](/README.md/) | [Próximo](Aula21.md) 

# Funções (Parte 1)

Funções está ligada diretamente a rtina, ou seja, tem trechos de codigo que se repetem e uma função nada mais é do que um pedaço do código que a gente sempre chama a hora que for necessário.
para criar uma funçõa, usamos a palavra chave **def**   
Um exemplo simples de função sem parâmetro:  
```
def mostralinha():
    print('--------------------------------')
```
Quando eu precisar usar uma linha, eu uso a função que eu criei.  
```
mostralinha()
print('Funções')
mostrainha()

--------------------------------
Funções
--------------------------------
```
  
  Podemos também, passar parametros para as nossas funções: 
```
def titulo(msg)
    print('--------------------------------')
    print(msg)
    print('--------------------------------')

titulo('funções')
titulo('Python')
titulo('Simples')

--------------------------------
Funções
--------------------------------
--------------------------------
Pyton
--------------------------------
--------------------------------
Simples
--------------------------------
```
  
Usando Funções com operações aritméticas:  
```
def soma(a, b):
    print(a + b)

soma(3, 4)
```
Podemos alterar a ordem das variáveis na funão
```
def soma(a, b):
    print(a + b)

soma(b = 3, a = 4)
```
  
Nestes exemplos, é obrigatório colocar 2 parâmetros, para isso usamos o que é chamaod de **empacotamento**  
```
def contador(*num):
    print(num)

contador(1, 3, 5)
contador(2, 3, 1, 4, 6, 5)

(1, 3, 5)
(2, 3, 1, 4, 6, 5)
```
O **(* num)** cria uma tupla na função e tudo que é possivel fazer em tuplas, podemos fazer na função também  
É possivel trabalhar com listas também nas funções  
```
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(lst)

valores = [6, 3, 9, 1, 0, 5]
print(valores)
dobra(valores)

[6, 3, 9, 1, 0, 5]
[12, 6, 18, 2, 0, 10]
```
```
def soma(* valores):
    s=0
    for num in valores:
        s += num
    print(f'A soma dos valores {valores} é {s}')

soma(5, 2)
soma(2, 9, 4)

A soma dos valores (5, 2) é 7
A soma dos valores (2, 9, 4) é 15
```  
  
[Exemplos Aula 20](Aula20.py)