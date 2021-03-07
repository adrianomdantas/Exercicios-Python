from datetime import date
menor = 0
maior = 0
for c in range(1,8):
    ano = int(input('Digite o {}o ano '.format(c)))
    if date.today().year - ano < 21:
        menor += 1
    else:
        maior += 1
print('Ao todo, {} pessoas ainda não atingiram a maioridade'.format(menor))
print('Ao todo, {} pessoas já atingiram a maioridade'.format(maior))       
