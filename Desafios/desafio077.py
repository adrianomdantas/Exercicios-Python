palavras = ('aprender','programar','linguagem','python','curso','gratis','estudar','praticar','trabalhar','mercado','programador','futuro')
for i in palavras:
    print(f'\nA palavra {i.upper()} temos', end=' ')
    for a in i:
        if a in 'aeiou':
            print(f' {a} ', end='')
print('')        