conta = 0
cont = 0
for impar in range(1, 500):
    if impar %3 == 0 and impar % 2 != 0:
        conta = conta + impar
        cont += 1
print(conta, cont)
