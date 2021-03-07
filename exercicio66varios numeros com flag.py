s = c = 0
while True:
    n = int(input('Digite um numero (999 para parar) '))
    if n == 999:
        break
    s += n
    c += 1
#print('A soma vale{}'.format(s))
print(f'A soma vale {s} e foram digitados {c} numeros')
