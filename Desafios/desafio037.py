n1 = int(input('Digite um numero e escolha uma opção: '))
print('( 1 ) converter para Binário:')
print('( 2 ) converter para Octadecimal:')
print('( 3 ) converter para Hexadecimal:')
op = int(input('Digite uma opção: '))
if op == 1:
    print(f'O Numero {n1} em binário fica: ', bin(n1)[2:])
elif op == 2:
    print(f'O Numero {n1} em Octadecimal fica: ', oct(n1)[2:])
elif op == 3:
    print(f'O Numero {n1} em Hexadecimal fica: ', hex(n1)[2:])
else:
    print('Opção errada!!!')