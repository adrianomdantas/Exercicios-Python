def notas(* n, sit=False):
    """
    -. Verifica a situação da turma
    :param n: notas alunos
    :param sit: valor opcional
    :return; dicionário com várias informações
    """
    turma = {}
    qtdnotas = len(n)
    maxnota = n[0]
    minnota = n[0]
    media = 0
    for i in n:
        if i < minnota:
            minnota = i
        if i > maxnota:
            maxnota = i
        media += i
    media = media / qtdnotas
    turma['total'] = qtdnotas
    turma['Maior'] = maxnota
    turma['Menor'] = minnota
    turma['Média'] = media
    if sit:
        if media <= 5:
            turma['situação'] = 'Ruim'
        elif 5 < media < 7:
            turma['sutiação'] = 'Razoável'
        else:
            turma['situação'] = 'Boa'
    return turma
    
resp = notas(2, 0, 0, 1, 5)
print(resp)
total = notas(2, 0, 0, 1, 5, sit=True)
print(total)
