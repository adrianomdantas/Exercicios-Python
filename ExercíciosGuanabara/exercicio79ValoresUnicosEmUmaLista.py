numeros = list()
while True:
    n = (int(input('Digite um numero ')))
    if n in (numeros):
        print('Valor duplicado, não vou adicionar ...')
    else:
        numeros.append(n)
        print('Numero cadastrado com sucesso ...')
    fim = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    while fim not in 'SN':
        fim = str(input(' tente novamente. Deseja continuar?[S/N] ')).strip().upper()[0]
        if fim == 'N':
            break
    if fim == 'N':
        break
print('=-' * 30)
numeros.sort()
print(f'Você digitou os valores {numeros}')
   
