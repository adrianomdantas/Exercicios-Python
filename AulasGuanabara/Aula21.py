#help()
#print(input.__doc__)

def contador(i, f, p):
    """
    Faz uma contagem e mostra na tela
    :param :i Inicio da contagem
    :param :f Fim da contagem
    :param :p Passo da contagem
    :return: sdem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='')
    print('FIM!')



help(contador)