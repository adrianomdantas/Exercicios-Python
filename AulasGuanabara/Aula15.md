[Anterior](Aula14.md) | [Menu Principal](/README.md/) | [Próximo](Aula16.md)  

# Interrompendo repetições while  

Normalmente em outras linguagens de programação existem 3 estruturas de repetição, For, While e repete, porém no Python não existe a repete, mas não é por isso que não dê para usar esta funcionalidade no Python, é o **do while**  
Por exemplo:  
```
while True:
    condição
        codigo
        break
``` 
Quando você usa o **break**, o loop é interrompido, ou seja, este loop é infinito até que uma consição usa o comando break.  
Exemplo, para interromper um loop de somas de número sem somar a flag '999'.   
```
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')
```
Quando o comando break é executado, o loop é interrompido imediatamente

OBS:  
A partir do Python 3.6, foi implementado o uso das F strings  
```
# formas de escrever o format (f strings)
# nome = 'josé'
# idade = 33
# print(f'O {nome} tem {idade} anos') Python 3.6 +
# print('O {} tem {} anos.' format(nome, idade) Python 3
# print('O %s tem %d anos.' % (nome, idade)) Python  2
```
Todas as formas ainda funcionam, porém é indicado usar sempre a ultima versão, mas se o python for masiantigo, será obrigatório a usar as formas masi antigas.


[Exemplos Aula 15](Aula15.py)