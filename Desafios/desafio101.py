def voto(anonasc):
    from datetime import date
    anoatual = date.today().year
    if anoatual - anonasc < 16:
        return f'Com {anoatual - anonasc} anos: VOTO NEGADO'
    elif 17 < anoatual - anonasc < 66:
        return f'Com {anoatual - anonasc} anos: VOTO OBRIGATÓRIO'
    else:
        return f'Com {anoatual - anonasc} anos: VOTO FACULTATIVO'

print(20 * '-')
nascimento = int(input('Digite o seu ano de nascimento: '))
print(voto(nascimento))
