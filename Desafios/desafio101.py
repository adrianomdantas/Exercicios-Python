def voto(anonasc):
    from datetime import date
    anoatual = date.today().year
    if anoatual - anonasc < 16:
        print(f'Com {anoatual - anonasc} anos: VOTO NEGADO')
    elif 17 < anoatual - anonasc < 70:
        print(f'Com {anoatual - anonasc} anos: VOTO OBRIGATÓRIO')
    else:
        print(f'Com {anoatual - anonasc} anos: VOTO FACULTATIVO')

nascimento = int(input('Digite o seu ano de nascimento: '))
voto(nascimento)
