ordem = list()
for c in range(0, 5):
    n = int(input('Digite um numro: '))
    if c == 0 or n > ordem[-1]:
        ordem.append(n)
        print('Numero adicionado na ultima posição')
    else:
        pos = 0
        while pos < len(ordem):
            if n <= ordem[pos]:
                ordem.insert(pos, n)
                print(f'Numero asdicionado na posiçao {pos}')
                break
            pos +=1
print('=-' * 30)
print(ordem)

'''ordem = []
for c in range(0, 5):
    num = int(input('Digite um numero: '))
    if c == 0 or num > ordem[-1]:
        ordem.append(num)
    else:
        pos = 0
        while pos < len(ordem):
            if num <= ordem[pos]:
                ordem.insert(pos, num)
                break
            pos += 1
                        
            
print(ordem)'''           

            
            


    
