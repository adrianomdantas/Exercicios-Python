n = int(input('digite um numero de 1 a 9999: '))
u = n % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('A unidade', u)
print('A dezena', d)
print('A centena', c)
print('A milhar', m)

