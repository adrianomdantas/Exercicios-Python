n1 = input('digite um numero de 1 a 9999: ')
tamanho = len(n1)
if tamanho == 1:
    print('a unidade é: ', n1)
if tamanho ==2:
    print('a dezena é: {1} \na unidade é:{0}'.format(n1[1], n1[0]))
if tamanho == 3:
    print('a centena é: {2} \na dezena é: {1} \na unidade é: {0}'.format(n1[2], n1[1], n1[0]))
if tamanho == 4:
    print('a milhar é: {3} \na centena é: {2} \na dezena é: {1} \na unidade é: {0}'.format(n1[3], n1[2], n1[1], n1[0]))
if tamanho >4:
    print('era para digitar só até 9999 cabeção')
    
