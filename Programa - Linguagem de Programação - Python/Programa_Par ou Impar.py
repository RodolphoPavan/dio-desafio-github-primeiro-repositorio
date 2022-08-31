numero = int(input())
if numero >= 2:
    resultado = numero % 2
    if resultado == 0:
        p1 = numero + 2
        i1 = numero - 1
        print(f'{i1} {p1}')
    else:
        p2 = numero + 1
        i2 = numero - 2
        print(f'{i2} {p2}')
else:
    print()
