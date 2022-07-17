opcao = 1
while opcao != 5:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    print(f'{7*"#"} menu {7*"#"}')
    print('[ 1 ] Soma')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Digitar novos números')
    print('[ 5 ] sair do programa')
    opcao = int(input('Digite uma opção: '))
    if opcao < 1 or opcao >5:
        while opcao < 1 or opcao > 5:  
            opcao = int(input('Opção errada, Digite uma opção: '))
    else:
        if opcao == 1:
            print(f'A Soma dos numeros é {n1 + n2}')
        elif opcao == 2:
            print(f'A multiplicação dos números é {n1 * n2}')
print('Finalizado')