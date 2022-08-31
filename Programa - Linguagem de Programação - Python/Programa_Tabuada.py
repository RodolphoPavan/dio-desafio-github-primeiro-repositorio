N = int(input()) #Entrada

if (0 <= N <= 10):
    contador = 1 
    
    while (contador <= 10): #loop
        print(f'{N} x {contador} = {N * contador}') #Saída
        
        contador = contador + 1 #vai somar 1 até chegar ao 10
