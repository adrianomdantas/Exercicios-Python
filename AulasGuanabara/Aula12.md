[Anterior](Aula11.md) | [Menu Principal](/README.md/) | [Próximo](Aula13.md)  

Na condição simples, utilizamos apenas um **if**, se acontecer umacondição, o programa toma uma decisão, se não acontecer não faz nada.  
Na condição composta, além do **if** usamos o **else**, ou seja, temos 2 opções para o programa toma sdecisão, si acontecer uma condição, o programatoma uma decisão, se não acontecer, o programa toma outra decisão.  
Mas e se tivermos mais de 2 condições par o programa tomar decisões?  
NEste caso usaremos o **elif** entre o **if** e o **else**.  
Exemplo:  
```
nome = str(input('Digite seu nome: '))
if nome == 'Fulano':
    print(f'Que nome bonito, Tenha um bom dia {nome}')
elif nome == 'Joao' or nome =='Maria':
    print(f'Seu nome é bem popular aqui no Brasil, Tenha um bom dia {nome}')
else:
    print(f'Tenha um bom dia {nome}')
```
É possível usar quantos Elif for necessário  

[Exemplos Aula 12](Aula12.py)
