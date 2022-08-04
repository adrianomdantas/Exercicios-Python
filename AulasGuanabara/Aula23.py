
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (TypeError, ValueError):
    print('Tivemos um erro com os tipos de dados que você digitou')
except ZeroDivisionError:
    print('Não é possível dividir por zero')
except KeyboardInterrupt:
    print('O usuário preferiu nãoinformar dados')
except Exception as erro:
    print(f'O erro foi{erro.__class__}') # Para identificar o tipo de erro
else:
    print(f'O resultado é {r}')
finally:
    print('volte sempre')