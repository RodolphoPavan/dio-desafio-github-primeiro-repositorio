lista = ['A', 'B', 'C', 'D', 'E', 'F','G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

N = int(input()) #1 Entrada

def exibe_letra(contador): #5 segundo contador na função
    posicao_letra = lista[contador - 1] #6 lista começa em 0

    i = 1

    while i <= contador:
        letra_alfabeto = posicao_letra * contador
        i += 1 #para não rodar em loop 

    print(letra_alfabeto)#Saída


if (1 <= N <= 26):
    i = 1 #2 primeiro_contador inicia em 1

    while (i <= N): #3 repete o primeiro_contador enquanto for menor ou igual a N
        exibe_letra(i)
        i += 1 #4 mais igual a 1, para não rodar em loop 
