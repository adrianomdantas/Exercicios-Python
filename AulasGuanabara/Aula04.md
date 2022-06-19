[Anterior](Aula03.md) | [Menu Principal](/README.md/) | [próximo](Aula05.md)

# Primeiros comandos em Python3

Estes serão os primeiros passos na linguagem Python, Mostrar na tela uma informação e solicitar uma informação para o usuário.

No Python, para você mostrar algo na tela, para mostrar um amensagem na tela, o comando `print()` e é necessário usar aspas(simples ou duplas) para exibir um texto, porém para exibir o conteúdo de uma variável, não devem ter as aspas como nos exemplos abaixo  
```
pythpn
>>> print('Olá Mundo!')
Olá Mundo!

>>> variavel = 'teste'
>>> print(variavel)
teste

>>> print(7+4)
11
>>>

>>> print('7'+'4')
74

>>> print('olá'+5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str

>>> print('olá',5)
olá 5
```
Como deu para perceber, o símbolo '+' serve para uma função a parte de somar, serve para juntar 2 strings, assim como a vírgula ',' também, porém a vírgila não junta doistipos diferentes de dados, neste caso é necessário usar o '+'.  

Usand um pouco mais de variáveis agora  
```
>>> idade = 42
>>> peso = 65
>>> nome = 'Fulano'
>>> print(nome,idade,peso)
Fulano 42 65
```
Agora, ao invés de deixar as variaveis preenchidas, vamos solicitar as informações ao usuário
```
>>> nome = input('Digite o seu nome: ')
Digite o seu nome: Ciclano
>>> idade = input('Digite a sua idade: ')
Digite a sua idade: 30
>>> peso = input('Digite seu peso: ')
Digite seu peso: 80
>>> print('O peso do '+nome+' é '+peso+' e sua idade é '+idade)
O peso do Ciclano é 80 e sua idade é 30
>>>
```
Mas não é muito interessante fazer desta forma, vamos fazer usando o IDLE (instalado junto com o python)  
Abra o IDLE  
![](/Imagens/aula4-img01.png)  
Logo após abrir, digite *CRTL+N* ou clique em *file* e depois em *New FIle*  
![](/Imagens/aula4-img02.png)  
digite seu código e aperte *f5*, ou clique em *Run* e depois em *Run Module*, será solicitado para você salvar oprojeto para poder rodar o script  
![](/Imagens/aula4-img03.png)  

Você pode voltar na primeira página do IDLE e testar quantas vezes quiser.