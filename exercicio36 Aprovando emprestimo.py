vcasa = float(input('Qual o valos da casa? R$'))
salario = float(input('Qual o salario do comprador? R$'))
anos = float(input('Quandtos anos você pretence pagar a casa? '))
prestacao = vcasa / anos /12
#salario30 = salario * 0.3
if salario * 0.3 > prestacao:
    print('seu salãrio é R${:.2f}, a prestação R${:.2f} parabens, emprestimo aprovado'.format(salario, prestacao))
else:
    print('seu salário é de R${:.2f}, e a prestação R${:.2f}, emprestimo negado'.format(salario, prestacao))
