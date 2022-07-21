valores = []
if len(valores) == 0:
    n = int(input('digite um valor: '))
    valores.append(n)
    print('Adicionado primeiro item a lista...')
for i in range(1, 5):
    n = int(input('digite um valor: '))
    if n > valores[-1]:
        valores.append(n)
        print('Adicionado ao final da lista...')
    else:
        for pos, val in enumerate(valores):
            if val > n:
                valores.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
print(20 * "=-")
print(f'Os valores digitados em ordem foram {valores}')