n1 = cont = soma = maior = menor = 0
parar = 's'
while parar in 'Ss':
    n1 = int(input('Digite um numero: '))
    soma += n1
    cont += 1
    if cont == 1:
        maior = n1
        menor = n1
    else:
        if n1 < menor:
            menor = n1
        if n1 > maior:
            maior = n1
    parar = str(input('Continuar?[s/n]  ')).strip()[0]
print('Média', soma / cont)
print('Maior', maior)
print('Menor', menor)
