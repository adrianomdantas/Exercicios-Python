'''def mostralinha():
    print(40 * '-')


mostralinha()
print('Python')
mostralinha()

#usando funções dentrode funções
def titulo(msg):
    mostralinha()
    print(msg)
    mostralinha()


titulo('Python')
titulo('Funções')
titulo('Simples')

#funçõa para soma 

def soma(a, b):
    print(a + b)

soma(3, 4)
soma(5, 5)
soma(2, 1)

def contador(*num):
    print(num)

contador(1, 3, 5)
contador(2, 3, 1, 4, 6, 5)'''

'''def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(lst)

valores = [6, 3, 9, 1, 0, 5]
print(valores)
dobra(valores)'''

def soma(* valores):
    s=0
    for num in valores:
        s += num
    print(f'A soma dos valores {valores} é {s}')

soma(5, 2)
soma(2, 9, 4)