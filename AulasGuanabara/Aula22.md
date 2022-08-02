[Anterior](Aula21.md) | [Menu Principal](/README.md/) | [Próximo](Aula23.md)  

# Módulos e Pacotes  

Quando seu programa começa a ficar muito grande mesmmo com funções, podemos separar o programa em modulos (outro arquivo), e para usar usar este modulos, podemos importar estes modulos, e quando temos.  
Exemplo de Módulo:  
![](/Imagens/aula21-img01)  

Em um arquivo chamado uteis.py colocamos as funções  
```
def fatorial(n):
    f = 1
    for c in range(1, n + 1):
        f*= c
    return f

def dobro(n):
    return n * 2

def triplo(n):
    return n * 3
```  
E o programa prindipal, importa estas funções deste modulo.  
```
import uteis


num = (int(input('Digite um valor: ')))
fat = uteis.fatorial(num)
print(f'O Fatorial de {num} é {fat}')
print(f'O dobro de {num} é {uteis.dobro(num)}')
```  
Podemos importar partes do múdulo, posso imortar apenas as funções que eu preciso  
```
from uteis import fatorial, dobro


num = (int(input('Digite um valor: ')))
fat = fatorial(num)
print(f'O Fatorial de {num} é {fat}')
print(f'O dobro de {num} é {dobro(num)}')
```
Quando importamos apenas as funções, não utilizamos mais o nome do modulo **fat = uteis.fatorial(num)** e sim apenas a função **fat = fatorial(num)**  
**OBS**  
    Não é recomendável importar apenas as funções, pois se tivermos mais modulos com nome de funções iguais, pode conflitar, portanto, deve-se tomar muito cuidado ao usar este modelo de importação.  

**Vantagens da Modularização**  
- ORganização do código  
- Facilidade na manutenção  
- Ocultação do código detalhado  
- Reutilização em outros projetos  

**Pacotes**  

Porém quando os programas são extremamentes grandes, apenas a modularização não é suficiente, então partimos para pacotes (em outras linguagens são chamados de bibliotecas)  
Quando um módulo começa a ficar muito grande, para não ccriarmos varios módulos e acabar desorganizado o código, usamos os pacotes, que é a separação dos módulos por assunto.  
![](/Imagens/aula22-img02.png)  

Para criar um Pacote, basta criaar uma pasta, no Python, toda pasta é considerada um pacote e depois separar os assuntos por pastas também.  
E dentro de cada pacote e modulo, teremos que ter um arquivo ```__init__.py```.  
![](/Imagens/aula22-img03.png)  

```
from Uteis import numeros

num = (int(input('Digite um valor: ')))
fat = numeros.fatorial(num)
print(f'O Fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')
```



[Exemplos Aula 22](Aula22.py)  
[Modulo Aula 22](uteis.py)  
[Pacote Aula 22](/AulasGuanabara/Uteis)
