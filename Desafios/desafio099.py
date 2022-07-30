def maior(* num):
    import time
    if len(num) < 1:
        d = 0
    else:
        d = num[0]
    print(15 * '=-')
    print('Analisando os valores passados ...')
    for i in range(0, len(num)):
        time.sleep(0.5)
        print(num[i], end=' ', flush=True)
        if num[i] > d:
            d = num[i]
    print(f'Foram analisados {len(num)} valores ao todo')
    print(f'O maior valor informado foi o {d}.')
    d = 0

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()