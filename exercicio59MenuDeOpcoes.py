opcao = 4
while opcao == 4:
    n1 = float(int(input('Digite o peimeiro numero: ')))
    n2 = float(int(input('Digite o segundo numero:')))
    resultado = 0
    opcao = int(input('[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos numeros\n[5]Sair do programa\n'))
    while opcao == 1:
        resultado = (n1 + n2)
        print('A soma é: ', resultado)
        opcao = int(input('\n\n[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos numeros\n[5]Sair do programa\n'))
    while opcao == 2:
        resultado = (n1 * n2)
        print('A multiplocação é: ', resultado)
        opcao = int(input('\n\n[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos numeros\n[5]Sair do programa\n'))
    while opcao == 3:
        lista = [n1, n2]
        print('O maior numero é: ', max(lista))
        opcao = int(input('\n\n[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos numeros\n[5]Sair do programa\n'))
    while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4  and opcao != 5:
        opcao = int(input('opção errada,digite 4 para recomeçar: '))
print('Fim')
