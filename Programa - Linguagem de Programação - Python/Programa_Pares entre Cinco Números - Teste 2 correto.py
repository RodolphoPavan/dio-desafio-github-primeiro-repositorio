contador = 1
divisor = 2
par = 0
impar = 0

while contador <= 5:
    valor = int(input())
    if  valor % divisor == 0:
        par += 1
        contador += 1
    else:
        impar += 1
        contador += 1

print(f'{par} valores pares')
