n1 = float(input('Digite a sua primeira nota'))
n2 = float(input('Digite a sua segunda nota'))
media = (n1 + n2)/2
if media < 5:
    print('sua media foi {}, portanto reprovado'.format(media))
elif media >=5 and media <=6.9:
    print('Sua média foi {}, você esta de revuperação'.format(media))
else:
    print('Parabens, você passou de ano')
