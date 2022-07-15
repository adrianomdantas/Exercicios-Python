cont = 0
primo = int(input('Digite um número para saber se ele e primo: '))
if primo < 2:
    (print(f'O número {primo} não é primo'))
else:
    for i in range(primo, 0, -1):
        if primo % i == 0:
            cont += 1
    if cont == 2:
        print(f'O número {primo} é primo')
    else:
        print(f'O número {primo} não é primo')
