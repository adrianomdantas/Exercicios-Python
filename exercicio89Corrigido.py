ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('nota 1: '))
    nota2 = float(input('nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    fim = str(input('Deseja continuar? ')).upper()[0].strip()
    while fim not in 'NS':
        fim = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if fim == 'N':
            break
    if fim == 'N':
        break
print(f'{"n°":<4}{"nome":<10}{"Média":>8}')
print('-'*30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('_'*30)
    opc = int(input('Mostrar notas de qual aluno? (999 encerra o programa: )'))
    if opc == 999:
        print('Encerando ...')
        break
    if opc <= len(ficha) - 1:
        print(f'notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< Volte sempre >>>')
                 
    
    

    

