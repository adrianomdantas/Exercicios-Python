nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print(f'média {media:.1f}, você está reprovado!!!')
elif media >= 5 and media < 7:
    print(f'média {media:.1f}, Você está de recuperação!!!')
else:
    print(f'média {media:.1f}, Parabéns, você foi aprovado!!!')