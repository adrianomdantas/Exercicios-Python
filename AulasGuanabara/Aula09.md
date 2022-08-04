[Anterior](Aula08.md) | [Menu Principal](/README.md/) | [Próximo](Aula10.md)  

# Manipulando Texto  

A manipulação de texto é uma das funções mais importantes no mundo da programação, principalmente para quem quer mexer com automação e tratar dados, planilhas etc ...  
Para atribuirmos uma frase a uma variável, basta usar aspas como mostrado abaiso  
```
frase = 'Estudar Python'
```
Porém o computador não guarda a frase inteira na memória, ele separa em pedacinhos mais ou menos assim  
|0|1|2|3|4|5|6|7|8|9|10|11|12|13|
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|E|s|t|u|d|a|r||P|y|t|h|o|n|  

Já podemos enxergar o fatiamento ai, se quesermos exibir na tela apenas uma letra, podemos  
```
print(frase[5])
>>> a
```
Esta é a forma mais simples de fatiamento.  
Note que a primeira posição começa com zero"0" e não com um"1".  
Outra forma de fatiamento é pegar um trecho de um texto ou uma frase como por exemplo  
```
print(frase[5:10])
>>> ar py
```  
Note que apesar de ter o 10 no fatiamento, só foi mostrado até a letra 9, isso é por conta que o Python sempre desconsidera a ultima letra, logopara você pegar a ultima letra, ou você seleciona um número a mais (14) ou apenas deixar sem nada que é o mais recomendado.  
Outra forma de fatiamento seria  
```
print(frase[5:14:2])
>>> a yhn
```  
Perceba que além de fatiar da letra 5 pra frente, estamos pulando de 2 em 2 letras  
A frase pode ser fatiada até certo ponto também   
```
print(frase[:5])
>>> Estud
```
Neste caso vale a regra que o python não exibe a ultima letra.  

Vamos nos aprofundar mais e começar a analisar a frase, por exemplo ver o tamanho da frase  com o comando **len()** que vem de length(comprimento)
```
print(len(frase))
>>> 14
```   
Poidemos contar os caracteres também com o comando **count()**
```
print(frase.connt('t'))
>>> 2
```  
E contagem já com fatiamento  
```
 print(frase.count('t',0,10))
 >>> 1
```  
Lembrando que, como o segundo "t" está na posição 10 e o Python não considera a ultima letra  
A função find também é importante  
```
print(frase.find('Py'))
>>> 8
```  
Ele vai mostrar aonde começou o que a gente está procurando, podemos usar isso com palavras, parte de palavras ou uma única letra  
E quando a gente procurar algo que não tem na frase? o Pythons simplesmente vai retornar o valor -1  
Para procurar a palavra **Estudar** na frase, podemos usar o comando ('Estudar' in frase), caso ele ache, vai retornar **True** e **False** se não encontrar  
E se quisermos trocar uma palavra da frase, também é possível usando o comando **replace()**  
```
frase.replace('Python','programação')
```
Não é uma mudança definitiva, apenas muda para o print.  
Para deixar toda a frase com letras maiúscilas  
```
print(frase.upper())
>>> ESTUDAR PYTHON
```  
E da mesma forma para deixar todo o texto com letras minúsculas.  
```
print(frase.lower())
estudar python
```  
Uma função interessante é o **captalize()** ele deuxa apenas a primeira letra maiúscula.  
```
print(frase.capitalize())
>>> Estudar python
```  
Outra função interessante é a função **title()**, todo começo de palavra fla em maiúscula  
```
print(frase.title())
>>> Estudar Python
```  
Para economizar espaço na memória e muitas vezes evitar erro no sistema, é importante eliminarmos os espaços de antes e depois da frase digitada, pra isso usamos o comando **strip()**  
Similares **rstrip()** elimina apenas os espaços da direita e o **lstrip()** elimina os espaços apenas da esquerda.  

O comando **split()** separa uma frase em varias palavras independentes, transforma a frase ou texto em palavras dentro de uma lista, o separador padrão são os espaços entre as palavras, porém, isso pode ser mudado  
```
print(frase.split())
>>> ['Estudar', 'Python']
```
Para eliminar espaços antes e apos dados digitados  
```
print(frase.strip())
```  

Da mesma forma que podemos separar, podemos juntar e ainda escolher o separados de palavras  
```
separar = frase.split()
juntar = '-'.join(separar)
print(juntar)
>>> Estudar-Python
```  

Função **print()** para texto, para printar na tela um texto inteiro, basta usar 3 aspas duplas como no exemplo  
```
print("""While The Python Language Reference describes 
the exact syntax and semantics of the Python language, 
this library reference manual describes the standard library 
that is distributed with Python. It also describes some of the 
optional components that are commonly included in Python distributions.""")
```


[Exemplos Aula 09](Aula09.py)

