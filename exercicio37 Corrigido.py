num = int(input('Digite um numero: '))
print('''Escolha uma das bases para conversão
[ 1 ] converter para binario
[ 2 ] converter para octal
[ 3 ] converter para hexadecimal''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para binario é {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} cinvertido para octal é {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Você digitou a opção errada')

