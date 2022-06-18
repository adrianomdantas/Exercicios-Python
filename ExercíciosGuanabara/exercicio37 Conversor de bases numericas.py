n1 = int(input('Digite um numero: '))
opcao = int(input('digite uma opção \n1-binario \n2-octadecimal \n3-hexadecimal \nopção: '))
if opcao == 1:
    n1 = bin(n1)
elif opcao == 2:
    n1 = oct(n1)
elif opcao == 3:
    n1 = hex(n1)
else:
    print('Você digitou a opção errada')
print(n1:2)
