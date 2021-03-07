op = int(input('Quantos itens da sequencia de fibonacci você quer ver: '))
n1 = 0
n2 = 1
n3 = 0
c = 0
print(n1, end=' ')
while c < op:
    print(n2, end = ' ')
    n1 = n2
    n2 = n3
    n3 = n1 + n2
    c += 1
    
