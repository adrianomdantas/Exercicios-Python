teste = list()
teste.append('Adriano')
teste.append('42')
print(teste)
#['Adriano', '42']
'''galera = list()
galera.append(teste)
print(galera)
#[['Adriano', '42']]
teste[0] = 'João'
teste[1] = 22
galera.append(teste)
print(galera)'''
#[['João', 22], ['João', 22]] não foi usado o [:]
galera = list()
galera.append(teste[:])
print(galera)
teste[0] = 'João'
teste[1] = 22
galera.append(teste[:])
print(galera)
#[['Adriano', '42'], ['João', 22]]
#declarando varias listas dentro de uma lista
galera2 = [['João', 19], ['Ana',33], ['Joaquim', 13], ['Maria ', 45]]
print(galera2)
#[['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria ', 45]]
print(galera2[0])
#['João', 19]
print(galera2[0][0])
#João
for g in galera2:
    print(g)
'''
['João', 19]
['Ana', 33]
['Joaquim', 13]
['Maria ', 45]'''
for g in galera2:
    print(g[0])
'''
João
Ana
Joaquim
Maria'''
for g in galera2:
    print(f'{g[0]} tem {g[1]} anos')
'''
João tem 19 anos
Ana tem 33 anos
Joaquim tem 13 anos
Maria  tem 45 anos'''
#Criando listas dentro de listas com dados do teclado
gal = list()
dad = list()
for i in range(0, 3):
    dad.append(str(input('Nome: ')))
    dad.append(int(input('Idade: ')))
    gal.append(dad[:])
    dad.clear()
print(gal)
'''
Nome: João
Idade: 32
Nome: Maria
Idade: 55
Nome: Daniel
Idade: 33
[['João', '32'], ['Maria', '55'], ['Daniel', '33']]'''
for i in gal:
    if i[1] > 18:
        print(f'{i[0]} é maior de idade')
    else:
        print(f'{i[0]} é menor de idade')
'''
Nome: João
Idade: 33
Nome: Ana
Idade: 11
Nome: Maria
Idade: 45

João é maior de idade
Ana é menos de idade
Maria é maior de idade
'''

