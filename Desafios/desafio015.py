km = float(input('Digite quantos Km foram percorridos: '))
dia = int(input('Digite por quantos dias o carro foi usado: '))
valdia = dia * 60
valkm = km * 0.15 
valfin = valkm + valdia
print(f'km rodados           {km:>5}')
print(f'dias utilizados      {dia:>5}')
print(f'total a pagar R$     {valfin:>5.2f}')