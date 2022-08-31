inicio = int(input())
fim = int(input())

quantidade_bissexto = 0

def eh_bissexto(ano, quantidade_bissexto):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(ano)
        quantidade_bissexto += 1

if (0 <= inicio <= fim <= 9999):
    while inicio <= fim:
        eh_bissexto(inicio, quantidade_bissexto)
        inicio += 1

    print(f'bissextos: {quantidade_bissexto}')
