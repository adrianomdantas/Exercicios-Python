from desafio107mod import moeda
 

p = float(input('Digite um valor R$'))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')    
print(f'Aumento de 10% temos {moeda.aumentar(p, 10)}')
print(f'Desconto de 13% temos {moeda.diminuir(p, 13)}')