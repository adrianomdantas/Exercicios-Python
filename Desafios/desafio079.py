valores = []
while True:
    if len(valores) == 0:
        n = int(input('Digite o primeiro número: '))
        valores.append(n)
        print('Prieiro valor digitado')
        print(20 * "=-")
    else:
        n = int(input('Digite um número: '))
        if n not in valores:
            if n > valores[-1]:
                valores.append(n)
                print('número dacastrado em ultimo')
                print(20 * "=-")
            else:
                for p, i in enumerate(valores):
                    if i > n:
                        valores.insert(p, n)
                        print('Valor cardastrado')
                        print(20 * "=-")
                        break
        else:
            print('numero não cadastrado, valor duplicado')
            print(20 * "=-")
    opcao = input('Dedeja continuar? [S/N] ').upper()
    print(20 * "=-")
    while True:
            if opcao not in 'SN':
                opcao = input('Dedeja continuar? [S/N] ').upper()
            else:
                break
    if opcao == 'N':
        break
print(f'Você digitou os valores{valores}')

