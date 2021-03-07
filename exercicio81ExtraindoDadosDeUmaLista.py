numeros = []
while True:
    numeros.append(int(input('Digite um numero: ')))
    fim = str(input('Deseja continuar [S/N]? ')).upper()[0].strip()
    while fim not in 'SN':
        print('Opção errada!!!')
        fim = str(input('Deseja continuar [S/N]? ')).upper()[0].strip()
        if fim == 'N':
            break
    if fim == 'N':
        break
print(f'Você digitou {len(numeros)} elementos')
numeros.sort(reverse=True)
print(f'Os valores digitados em ordem decrescente são {numeros}')
if 5 in numeros:
    print('O numero 5 faz parte da lista')
else:
    print('O numero 5 não faz parte da lista')
