divida = int(input())
pagamento_mensal = int(input())

contador = 0

while divida != 0:
    contador += 1

    if divida >= pagamento_mensal:
        antes_pagamento = divida
        divida = divida - pagamento_mensal
        depois_pagamento = divida
    else:
        antes_pagamento = divida
        divida = divida - divida
        depois_pagamento = divida

    print(f'pagamento: {contador}')
    print(f'antes = {antes_pagamento}')
    print(f'depois = {depois_pagamento}')
    print(f'-----')


