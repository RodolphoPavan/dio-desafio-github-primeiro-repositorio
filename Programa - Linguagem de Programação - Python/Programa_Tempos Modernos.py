Semana = input()        #Entrada "Digite o dia da Semana"
Entrega = int(input())   #Entrada "Quantidade de dias da entrega"

ListaDeDias = ['domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado']

if Entrega == 0: #Se for 0 "Chaga Hoje"
    print('chega hoje!')
elif Entrega <= 0: #Se for menor que 0, não aparece nada!
    print()
elif Entrega > 6: #Se for maior que 6, não aparece nada!
    print()  
else:
    indexDoDias = ListaDeDias.index(Semana) #criar uma lista, comando index
    novaLista = ListaDeDias[indexDoDias + 1:len(ListaDeDias)] + ListaDeDias[0:indexDoDias]
    Entrega = novaLista[Entrega - 1]
    print('sera entregue', Entrega)
