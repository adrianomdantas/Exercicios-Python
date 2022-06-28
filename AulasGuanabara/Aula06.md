[Anterior](Aula04.md) | [Menu Principal](/README.md/) | [Próximo](Aula07.md)

# Tipos Primitivos e Saída de Dados  

Quando a gente vai somar 2 letras teremos o resultado do exemplo  
```
 "a + b = ab"
 ```
 E há duas formas de enxergar numeros, como números e como letras logo quando somarmos 3 e 7, se considerados como letras, teremos o resultado
 ```
 3 + 7 = 37
 ```
Porém se considerarmos números, o resultado será diferente
```
3 + 7 = 10
```
Em python, em algumas ocasiões, temos que deixar pré extabelecido que usaremos números nas variáveis   
observe a palavra **"int"** antes do comando de solicitação de dados
```
n1 = int(input("Digite um número: ))
n2 = int(input("Digite mais um número: ))
s = n1 + n2
print(f'A soma vale {s}')
```
A função do **"int"** é exatamente estabelecer que aquela variável armanezará um número inteiro, logo quando formos fazer uma operação aritmética de soma ou subtração, estes números serão enxergados como números e a operação acontecerá, porém temos outros tipos primitivos.  
**int** (números inteiros)
**float** (numeros flutuantes que usam virgula, mas lembre-se que o python usa o pobto e não a vírgula)
**bool** (booleanos, que são verdadeiro ou falso, **True False**, obserte que as primeiras letras são maiúsculas)
**str** (string, que são para letras e palavras, necessário estar entre aspas)
Sempre que for necessário saber o tipo da variável, é simples, basta usar o exemplo abaixo  
```
print(type(variável))
```
Temos umas formas interessantes fazer um teste de tipo da informação que está na variável, pra isso a gente usa a sintaxe abaixo  
```
n = input('Digite algo: ')
print(n.isnumeric())
```
O retorno será sempre True ou False, lembrando que como estamos usando o input, a variável sempre será string, a menos que eu mude usando algum tipo na variável.

[Alguns exemplos de verificar o tipo do conteudo da variável](Aula06.py)

