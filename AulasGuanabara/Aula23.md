[Anterior](Aula22.md) | [Menu Principal](/README.md/)

# Tratamento de Erros e Exceções  

Os erros tratados nas Exceções, são erros que não são do código em si (sintaxe) por exemplo `primt(x)` erramos a digitação da palavra print, e sim por uma variável não declarada, ou quando uma variável tipada como int recebe uma intormação não esperada como float ou uma string.  
```  
print(x)

Traceback (most recent call last):
  File "C:/Users/Adriano/OneDrive/Área de Trabalho/teste.py", line 1, in <module>
    print(x)
NameError: name 'x' is not defined
``` 
NEste caso foi disparado uma excessão *NameError*.  
Ou por exemplo, uma divisão por 0 "zero":  
```
a = int(input('Numerador: '))
b = int(input('Denominador: '))
r = a / b

>>> Numerador: 8
>>> Denominador: 0

Traceback (most recent call last):
  File "C:/Users/Adriano/OneDrive/Área de Trabalho/teste.py", line 3, in <module>
    r = a / b
ZeroDivisionError: division by zero
```
Perceba que foi disparado a exceção *ZeroDivisionError: division by zero*, na linha 3 foi tentado uma divisão por zero.  
Ou ainda:  
```
n = int(input('Digite um número '))
print(n)

Digite um número g
Traceback (most recent call last):
  File "C:/Users/Adriano/OneDrive/Área de Trabalho/teste.py", line 1, in <module>
    n = int(input('Digite um número'))
ValueError: invalid literal for int() with base 10: 'g'
```  
Disparado uma excessão de valor, a variavel estava tipada como int e recebeu uma string.  
Outras excessões são comuns como tentar acessar um indice que não existe na lista ou importar um módulo que não existe.  
São inúmeras [exceptions](https://docs.python.org/3/library/exceptions.html)  


Para tratar estas exceções, usamos os comandos **try/except**  
```
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except:
    print('Tivemos um erro')
else:
    print(f'O resultado é {r:.1f}')

#sem erro
Numerador: 8
Denominador: 4
O resultado é 2.0

#com erro
Numerador: 8
Denominador: 0
Tivemos um erro
```  
E podemos usar ainda o comando **finally**  
```
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except:
    print('Tivemos um erro')
else:
    print(f'O resultado é {r}')
finally:
    print('volte sempre')

#sem erro
Numerador: 8
Denominador: 2
O resultado é 4.0
volte sempre

#com erro
Numerador: tr
Tivemos um erro
volte sempre
```  
Quando você tiver programando, você pode usar várias exceptions e usar um Exception para saber o tipo de erro que está ocorrendo:  
```
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (TypeError, ValueError):
    print('Tivemos um erro com os tipos de dados que você digitou')
except ZeroDivisionError:
    print('Não é possível dividir por zero')
except KeyboardInterrupt:
    print('O usuário preferiu nãoinformar dados')
except Exception as erro:
    print(f'O erro foi{erro.__class__}') # Para identificar o tipo de erro
else:
    print(f'O resultado é {r}')
finally:
    print('volte sempre')
```

[Exemplo da Aula 23](Aula23.py)







