km = int(input('Qual a distancia da ssua viagem? '))
if km > 200:
    print('sua viagem vai custar R${:.2f} '.format(km*0.45))
else:
    print('Sua viagem vai custar R${:.2f}'.format(km*.50))
