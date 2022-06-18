n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [1]Somar
    [2]Multiplicar
    [3]Maior
    [4]Novos numeros
    [5]Sair do programa''')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        produto = n1 * n2
        print('O resultado de {} X {} é {}'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1> n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('informe o numero correto')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('finalizando ...')
    else:
        print('Opção invalida, tente novamente: ')
    print('=-='*10)
print('Fim do programa')
