from desafio108mod import moeda

p = float(input('Digite um valor: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumendtando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')