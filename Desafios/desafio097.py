def escreva(texto):
    tam = int(len(texto) + 4)
    print(tam * '~')
    print(f'  {texto}')
    print(tam * '~')


escreva('Palavra')    
escreva('Uma pequena frase')
escreva('Uma frase maior para teste')