n1 = float(input('digita a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
media = (n1+n2)/2
if media >= 7:
    print('A media deste aluno é: {}, aprovado'.format(media))
else:
    print('A média deste aluno é: {}, reprovado'.format(media))

