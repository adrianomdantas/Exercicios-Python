[Anterior](Aula20.md) | [Menu Principal](/README.md/) | [Próximo](Aula22.md) 

# Funções (Parte 2)  

- **Interactive Help** Ajuda interativa  
- **Docstrings** documentção do programa  
- **Argumentos opcionais**  a função sem necessidade de um nomero exato de argumentos
- **Escopo de variaveis** Quando uma variavel nasce ou morre

**Interactive Help**  

Além da documentação da linguagem e dos comandos, o Python tem uma ajuda interativa, basta usar o comando **help()**  
```
help()

Welcome to Python 3.8's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.8/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> print

Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
(END)
```
Para sair da ajuda interativa digite **quit**  
Outra forma de usar esta interatovodade é usando o **__doc__**  
```
print(print.__doc__)

print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

Prints the values to a stream, or to sys.stdout by default.
Optional keyword arguments:
file:  a file-like object (stream); defaults to the current sys.stdout.
sep:   string inserted between values, default a space.
end:   string appended after the last value, default a newline.
flush: whether to forcibly flush the stream
```  
  
**Docstring**  
  
Todas as funcionalidade do Python tem usuas docstring, e é recomendável fazer as nossas docstrings também, basta abrir e ferar 3 aspas simples logo abaixo do comando def e explicar a funcionalidade da função que você criou.  
```
def contador(i, f, p):
    """
    Faz uma contagem e mostra na tela
    :param :i Inicio da contagem
    :param :f Fim da contagem
    :param :p Passo da contagem
    :return: sdem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='')
    print('FIM!')



help(contador)

Help on function contador in module __main__:

contador(i, f, p)
    Faz uma contagem e mostra na tela
    :param :i Inicio da contagem
    :param :f Fim da contagem
    :param :p Passo da contagem
    :return: sdem retorno
(END)
```
  
**Parametros Opcionais**  
  
Quando criamos uma função para 3 parametros e no codigo passamos apenas 2, ocorre um erro, por isso é importante este conceito de parametro opcional, nos setamos um valor para o parametro e caso não seja passado este parametro, a função considera a que foi setada na criação da função.  
```
def somar(a, b, c=0):
    s = a + b + c 
    print(f'A soma vale{s}')
```  
Perceba que o parametro "c" está valendo 0, caso não seja fornecido, a função considera este valor e não dá erro e nem altera o valor final, porém se for passado apenas um parametro, o erro ocorrerá, pois setamos apenas o parametro c, poderiamos deixar todos seados
```
def somar(a=0, b=0, c=0):
    s = a + b + c 
    print(f'A soma vale{s}')
```  
Agora mesmo sem não for passado nenhum parâmetro, a fução funciona, o erro só ocorrerá se forem passados mais de 3 parametros.  
Neste caso poderiamos usar multiplos parâmetros com **def somar(* var)**.  
  
**Escopo de variáveis**  
  
As variáveis podem ser globais (usadas em todo programa) ou locais(usadas apenas naquele pedaço do programa ou função)  
  
Exemplo de variável local.  
![](/Imagens/imgaula21doc01.png)  
  
Perceba que no programa acima, a variável **a** que está dentro da função, é local e será usada somente dentro da função, e não será considerada a variável **a** que está fora da função 

Exemplo de variável global  
![](/Imagens/imgaula21doc02.png)  
  
Neste caso, usando a palavra global dentro da função, estaremos considerando a variavel global dentro da função no escopo local.  
  
**Retorno de valores**  
  
As funções gralmente trabaha nos bastodires, e não printa nada na tela, elas retornam valorem par que o programa manipulem estes valores, por exemplo:  
```
def soma(a=0, b=0, c=0):
    s = a + b + c
    return s
    
r1 = soma(3, 2, 5)
r2 = soma(2, 3)
r3 = soma(6)
```  
O valor não é printado na tela, porém o valor é armazenado em uma variável, assim o progrma pode maniplar a informação ou até mesmo ser usado em outra função.  
Retornando True ou False.  
``` 
def par(a):
    if 0 % 2 == 0:
        return True
    else:
        return False

num = (int(input('Digite um número: ')))
par(num)
print(par(num))

# o retorno será True ou False
```  
  
Podemos retornar, tuplas, listas e Dicionários por exemplo.  
As possibilidades são inúmeras.



[Exemplos Aula 21](Aula21.py)