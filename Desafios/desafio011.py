alt = float(input('Digite a altura da parede em metros: '))
larg = float(input('Digite a largura da parede: '))
area = alt * larg
print(f'A área da parede é {area:.2f}m² e será necessário {area / 2:.1f} latas de timta para cobri-la')