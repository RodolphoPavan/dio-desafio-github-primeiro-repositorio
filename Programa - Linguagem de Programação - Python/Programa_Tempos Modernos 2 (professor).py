#Tempos modernos 2

domingo segunda terça quarta quinta sexta sábado domingo segunda terça quarta quinta sexta sábado
    0      1      2      3      4     5     6       7       8      9     10     11     12    13

dia = input() #terça
if dia == 'domingo':
    dia_numero = 0
elif dia == 'segunda':
    dia_numero = 1

prazo = int(input())
if prazo == 0:
    ....
else:
    entrega = dia_numero + prazo

    if entrega >= 7:
        entrega = entrega - 7
    if entrega == 0:
        ...
    elif entrega == 1:
        
