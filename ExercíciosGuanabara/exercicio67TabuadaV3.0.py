n = int(input('Qual tabuada você quer ver? '))
while n >= 0:
    if n < 0:
        break
    else:
        for m in range(1, 11):
            print(f'{n} X {m} = {n * m}')
        n = int(input('Qual tabuada você quer ver? '))
        print(30*'-')
