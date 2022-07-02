[Anterior](Aula07.md) | [Menu Principal](/README.md/) | [Próximo](Aula09.md)  

# Utilizando Módulos  

Módulos são na verdade agregados, uma epécie de acessórios da linguagem que nos ajudam com algumas funcionalidades no programa, é um pacote de codigos que já está pronto np python, e estes módulos fazem parte de bibliotecas, para poder usa-las nos importamos para o nosso programa, você pode importar a biblioteca inteira ou apenas o módulo que pretende usar.  
Uma exemplo é a biblioteca math.  

- **Math**
    - **ceil**      arredondar um número flutuante para cima
    - **floor**     arredondar um número flutuante para baixo
    - **trunc**     número exato eliminando o que vem após a vírgula
    - **pow**       função potência, similar aos 2 asteristicos
    - **sqrt**      função raiz quadrada
    - **factorial** calculo de fatorial

No momento que a gente usa o `import math`, automaticamente importamos todas as funcionalidades da biblioteca, mas se você quiser usar apenas uma das funcionalidades e não quer importar tudo, você pode importar apenas o que vai usar como por exemplo, vamos supor que vocçe vai usar apenas a raiz quadrada, então você vai usar `from math import sqrt`, pronto, apenas a funcionalidade de raiz quadrada foi importada da biblioteca math, você também pode importas apenas duas funcionalidade, tres ou quantas quiser, basta separar as funionalidade por vírgula `from math import sqrt, ceil`, veja que importamos além da raiz quadrada o arredondamento para cima.  
Segue um exemplo de ulitização importando toda a biblioteca:  
```
import math

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
#Mostrando a raiz calculada
print(f'A raiz de {num} é {raiz}')
#Usando outra função da biblioteca para arredondar o valor da raiz para cima
print(f'A raiz de {num} é {math.ceil(raiz)}')
```
Agora um exemplo usando apenas as funções que serão usadas no programa  
```
from math import sqrt

num = int(input('Digite um número: '))
raiz = sqrt(num)
print(f'A raiz de {num} é {raiz}')
```
Repare que agora eu não precisei usar math.sqrt() e sim usei direto o sqrt() devido eu ter importado apenas a função que eu queria usar.  

E como descobrir as bibliotecas que podemos importar?  
Basta você ir em [python.org](https://www.python.org/) e clicar em Documentation  
![](/Imagens/imgaula8doc01.png)  
Depois cliet=que neste botão amarelo python docs  
![](/Imagens/imgaula8doc02.png)  
Agora é só escolher a versão do python que você quer e clicar em **Library Reference**  
![](/Imagens/imgaula8doc03.png)  
Pronto, aqui é um mundo gigantesco a se explorar  
![](/Imagens/imgaula8doc04.png)  

Apesar de ser muito difícil nao tere algum modulo pronto, você pode fazer um e disponibilizar na internet para outras pessoas utilizarem assim como você pode usar qualquer biblioteca que esteja disponível, porém, se você for usar alguma biblioteca que já não venha nativo com o python (bibliotecas externas), será necessário instalar a biblioteca que você pretende usar, geralmente assim que você importar a biblioteca, o proprio console que você estiver usando (Pycarm, Visual Code, etc ...) vai te ajudar a instalar.


[Exemplos Aula 08](Aula08.py)