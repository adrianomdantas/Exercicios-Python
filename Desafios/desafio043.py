altura = float(input('Digite sua Altura em mertros: '))
peso = float(input('Digite seu peso em kg: '))
imc = peso / (altura**2)
if imc < 18.8:
    print(f'Seu IMC é {imc:.2f}, você está abaixo do peso')
elif 18.8 < imc <= 25:
    print(f'Seu IMC é {imc:.2f}, você está com o peso ideal')
elif 25 < imc <= 30:
    print(f'Seu IMC é {imc:.2f}, você está com sobrepeso')
elif 30 < imc <= 40:
    print(f'Seu IMC é {imc:.2f}, você está com obesidade')
else:
    print(f'Seu IMC é {imc:.2f}, você está com obesidade morbida')