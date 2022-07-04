# minha solução
frase = input('Digite uma frase qualquer: ')
cont = frase.count('a')
primeira = frase.find('a')
ultima = frase.rfind('a')
print(f'Esta frase tem {cont} letras "a"')
print(f'a Lestra "a" aparece pela primeira vez na posição {primeira}')
print(f'a Lestra "a" aparece pela ultima vez na posição {ultima}')

# solução Guanabara
# frase = str(input('Digite uma frase: ')).upper().strip()
# print('a letra a aparece {} vezes na frase.'.format(frase.count('A')))
# print('A primeira letra a apareceu na posição {}'.format(frase.find('A')+1))
# print('A ultima letra a apareceu na posição {}'.format(frase.rfind('A')+1))
