extenso = ('ZERO','UM','DOIS','TRES','QUATRO','CINCO','SEIS','SETE','OITO','NOVE','DEZ','ONZE','DOZE','TREZE','QUATORZE','QUINZE','DEZESEIS','DEZESETE','DEOITO','DEZENOVE','VINTE')
numero = int(input('Digite um número de 0 a 20: '))
while True:
    if numero < 0 or numero > 20:
        numero = int(input('!!ERRO!! Digite um número de 0 a 20: '))
    else:
        break
print(f"Você digitou o número {extenso[numero]}")