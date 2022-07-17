[Anterior](Aula11.md) | [Menu Principal](/README.md/) | [Próximo](Aula13.md)  

# Estrutura de repetição while  

Existe outrotipo de estrutura de repetição no Python, o **while**, é usado para quando precisamos de um loop infinito a menos que aconteça alguma condição, O for é uma estrutura de repetição que já existe uma liitação prévia, o while não, é interrompido por algum comando ou condição, mas não é por isso que não exista loops que évpossivel fazer com as duas estruturas de repetição, vai do programador decidir qual é melhor e se encaixa melhor para a situação.  
Exemplo:  
```
#Exemplo 1 com for
for c in range(1, 10):
    print(c, end='-')
print('fim')

#O mesmo com while
c = 1
while c < 10:
    print(c, end='-')
    c += 1
print('fim')
```
Perceba que são formas diferentes de estrutura de repetição para obter o mesmo resultado  
```
1-2-3-4-5-6-7-8-9-fim
1-2-3-4-5-6-7-8-9-fim
```
Neste caso que sabemos o limite (10), seria até mais interessante usar a estrutura for, mas e se tiver uma ocasião em que nãi sabemos o limite? ai neste caso o mais recomendado é usar o while.  
Imagina uma situação em que você quer solicitar numeros do usuário, mas você não sabe quantos umeros vão ser necessário? com o }For não seria possível, segue exemplo abaixo:  
```
n = 1
while n != 0:
    n = int(input('Digite um número ou "0" para interromper: '))
print('FIM')
```
Isto é chamado de **condição de parada**  
É comum criar uma condição em que o programa pergunte se você quer parar S/N  
```
r = 'S'
while r == 'S':
    n = int(input('Digite um número: '))
    r = input('Quer continuar? [s/n]: ').upper()
print('FIM')
```
Outro exemplo de uso do while é caso não digite o que for solicitado, continue o  loop  
```
# .strip() eliminar espaços e 
#.upper()[0] deixar a letra maiuscula e usar apenas a primeira letra caso o usuario digite mais que uma

sexo = str(input('Digite seu sexo [M / F]: ')).strip().upper()[0] while sexo not in 'MF':
    sexo = str(input('Opção errada, Digite seu sexo [M / F]: ')).upper()
print(f'Sexo {sexo} registrado com sucesso')
```

[Exemplos Aula 14](Aula14.py)