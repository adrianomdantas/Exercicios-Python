[Anterior](Aula09.md) | [Menu Principal](/README.md/) | [Próximo](Aula11.md)

# Condições (Parte 1)

A condição **"Se"** na lógica de programação, serve para te dar opções do que o programa vai fazer dependendoda situação no momento, por exemplo **Se** seu carro tem mais de 5 anos, **então** ele já não é mais tão novo.  
```
tempo = int(input('Quantos anos tem seu casso? '))
if tempo <= 3:
    print('carro novo')
else:
    print('Carro velho')
print('FIM")
```  
Perceba que temos duas condições, Se o Carro tiver menos de 3 anos, então o programa vai escrever que o carro é novo, e se tiver de 3 anos para cima, então o programa vai escrever que o carro não é mais novo.  
Um exemplo classico é o da media de um aluno.  
```
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2
if media >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
```
