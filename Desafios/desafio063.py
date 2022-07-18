n1 = 0
n2 = 1
n3 = 1
cont = 1
n = int(input('Digite quantos termos da sequencia de fibonacci você quer ver: '))
if n == 1:
    print(f'{n1}', end=' ')
elif n == 0:
    print('nenhum termo')
else:
    print(f'{n1}', end=' - ')
while cont < n:
    if cont == n-1:
        print(f'{n2}', end=' ')
        cont +=1
    else:
        print(f'{n2}', end=' - ')
        cont +=1
        n1 = n2
        n2 = n3
        n3 = n1 + n2
    
