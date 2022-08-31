p1 = input()
p2 = input()
p3 = input()

if p1 == 'vertebrado':
    if p2 == 'ave':
        if p3 == 'carnivoro':
            print('aguia')
        else: #onivoro
            print('pomba')
    else: #mamífero
        if p3 == 'onivoro':
            print('homem')
        else: #Herbivotro
            print('vaca')
else:
    if p2 == 'inseto':
        if p3 == 'hematofago':
            print('pulga')
        else: #herbivoro
            print('lagarta')
    else: #anelidio
        if p3 == 'hematofago':
            print('sanguessuga')
        else: #onivoro
            print('minhoca')
