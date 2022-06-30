[Anterior](Aula06.md) | [Menu Principal](/README.md/) | [Próximo](Aula08.md)

# Operadores Aritméticos  

Os operadores aritiméticos usados em Pyhon são:  

|Operadores|Função|
|-|:-|
|+|Soma|
|-|Subtração|
|*|Multiplicação|
|/|Divisão|
|**|Exponenciação|
|//|Divisão inteira|
|%|Resto da divisão|

Podemos usar os operadores aritméticoss com números mas também com strings para facilitar a nossa vida, e veja que para igualdade, vamos utilizar **==**
Alguns exemplos
```
5+2 == 7
5-2 == 3
5*2 == 10
5/2 == 2,5 (número flutuante)
5**2 == 25 (também pode ser usado a funçao pow(5,2))
5//2 ==2
5%2 == 1
```
**Ordem de Precedência**  

|Ordem|Operador|
|--|--|
|1|()|
|2|**|
|3|* / // %|
|4|+ -|

Exemplos:  
5 + 3 * 2 == 11  
3 * 5 + 4 ** 2 == 31  
3 * (5 + 4) ** 2 == 243   

**Calculando Raiz Quadrada ou Cubica**  

Para Calcular a Raiz qudrada você pode usar o exemplo:  
```
81 ** (1/2) == 9
27 ** (1/3) == 3
```
**Usando operadores co strings**

Para repetir uma letra ou símbolo varias vezes, basta usar o operador de multiplicação  

'#' * 20 == ####################  

Exemplo:  
```
print('#' * 20)
####################
```
Alguns exemplos de como usar o alinhamendo das palavras
```
nome = input('Digite Seu nome: ')
Digite Seu nome: Adriano

print('Prazer em te conhecer {}!'.format(nome))
Prazer em te conhecer Adriano!

print('Prazer em te conhecer {:20}!'.format(nome))
Prazer em te conhecer Adriano             !

print('Prazer em te conhecer {:>20}!'.format(nome))
Prazer em te conhecer              Adriano!

print('Prazer em te conhecer {:^20}'.format(nome))
Prazer em te conhecer       Adriano       

print('Prazer em te conhecer {:=^20}'.format(nome))
Prazer em te conhecer ======Adriano=======

```
Outros exemplos
```
n1 = int(input('Um valor: ')) 
n2 = int(input('Outro Valor'))
print('A soma vale {}'.format(n1+n2)) #quand o valor não será mais usado em oiutros lugares, podemos mostra-lo apaenas no print sem usar variavel
#Usando variáveis
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \nO produto é {}, a divisão é {:.2f}'.format(s, m, d), end= ' ') # o \n serve para quebrar a linha e o end='' para não quebrar a linha entre 2 prints
print('Divisão inteira {} e potência {}'.format(di, e))
```
 
[Exemplos Aula 07](Aula07.py)

