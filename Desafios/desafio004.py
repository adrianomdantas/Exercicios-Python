


algo = input('Digite Algo: ')
print('O tipo primitivo deste valor é: ',type(algo))
print('Só tem espaços? ', algo.isspace())
print('É um número? ', algo.isnumeric())
print('É Alfabético? ', algo.isalpha())
#usando o format
print(f'É Alfanumérico? {algo.isalnum()}')
print(f'Está em maiúscula? {algo.isupper()}')
print(f'Está em minúscila? {algo.islower()}')
print(f'Está captalizado? {algo.istitle()}')