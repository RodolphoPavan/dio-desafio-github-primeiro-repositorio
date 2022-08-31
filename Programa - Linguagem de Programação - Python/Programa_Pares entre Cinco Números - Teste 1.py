n1 = int(input()) 
n2 = int(input())
n3 = int(input()) 
n4 = int(input())
n5 = int(input()) 

divisor = 2
pares = 0
impar = 0

while divisor < n1:
    if n1 % divisor == 0:
        break
    divisor += 1
    
if divisor == n1:
    impar += 1
else:
    pares += 1

while divisor < n2:
    if n2 % divisor == 0:
        break
    divisor += 1
    
if divisor == n2:
    impar += 1
else:
    pares += 1

while divisor < n3:
    if n3 % divisor == 0:
        break
    divisor += 1
    
if divisor == n3:
    impar += 1
else:
    pares += 1

while divisor < n4:
    if n4 % divisor == 0:
        break
    divisor += 1
    
if divisor == n4:
    impar += 1
else:
    pares += 1

while divisor < n5:
    if n5 % divisor == 0:
        break
    divisor += 1
    
if divisor == n5:
    impar += 1
else:
    pares += 1
    
print(f'{pares} valores pares')
