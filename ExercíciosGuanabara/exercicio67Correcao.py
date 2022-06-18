while True:
    n = int(input('Qual tabuada você quer ver? '))
    if n < 0:
        break
    for m in range(1, 11):
        print(f'{n} X {m} = {n * m}')
    print(30*'-')
print('PROGRAMA DE TABUADA ENCERRADO!')
