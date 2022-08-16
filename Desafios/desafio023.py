

num = int(input('Digite um número até entre 1 e 9999: '))
print(f'Unidade: {num % 10}')
print(f'Dezena : {num % 100 // 10}')
print(f'Centena: {num % 1000 // 100}')
print(f'Milhar : {num % 10000 // 1000}') 
