n1 = 10
n2 = 5

if n1 % n2 > 1:
    soma = 3+5/n2
    if soma > 4:
        print(f'soma: {soma}')
else:
    if n1 / n2 > 1:
        n2 = n1 + 5
        print(f'n2: {n2}')
    else:
        n1 = n2 + 5
        print(f'n1: {n1}')
if 2 + n1/2*3>=18:
    n2=n2%n1
    print(f'n2: {n2}')
else:
    n1=n1%n2
    print(f'n1: {n1}')

print(f'{n1+n2}')
