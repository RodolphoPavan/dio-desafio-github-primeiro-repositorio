#VARIÁVEL CONTADORA
#Dados dois números inteiros p(=>0) e q(>0), exibir o quociente da divisão
#inteira de p por q sem usar operadores de divisão e multiplicação.

p = int(input('p: '))
q = int(input('q: '))
contador = 0
while p>= q:
    p = p - q #p -= q
    contador += 1
print(f'O quociente da divisão é {contador}')
