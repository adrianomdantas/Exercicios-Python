parar = 'S'
cont = 0
soma = 0
numero = int(input('Digite um número: '))
maior = menor = numero
cont += 1
soma += numero
parar = input('deseja digitar outro número [ S/N ]: ').upper()
while parar not in 'NS':
    parar = input('!! ERRO !! deseja digitar outro número [ S/N ]: ').upper()
while parar != 'N':
    numero = int(input('Digite um número: '))
    cont += 1
    soma += numero
    parar = input('deseja digitar outro número [ S/N ]: ').upper()
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    while parar not in 'NS':
        parar = input('!! ERRO !! deseja digitar outro número [ S/N ]: ').upper()
print(f'{5*"#"} FIM {5 * "#"}')
print(f'Foram digitados {cont} numeros')
print(f'O maior número digitado foi {maior}')
print(f'O menor número digitado foi {menor}')
print(f'A média dos numeros digitador é {soma / cont:.2f}')