n1 = int(input('Você quer saber a tabuada de qual número? '))
for i in range(1, 11):
    print(f'{n1:>3}  x{i:>3}  = {n1 * i:>3}')
