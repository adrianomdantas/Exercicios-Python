velo_carro = int(input('Digite a velocidade do carro em km: '))
Velocidade_permitida = int(80)
v_exce = velo_carro - Velocidade_permitida
if velo_carro > Velocidade_permitida:
    print(f'Você foi multado por exceder a velocidade permitida em {v_exce}km/h')
    print(f'O valor da multa a ser paga é de R${v_exce * 7:.2f}')
else:
    print('Velocidade dentro dos limites')