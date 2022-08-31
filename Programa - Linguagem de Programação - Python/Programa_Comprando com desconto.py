PREÇO = float(input())
COMPRA = int(input())
TOTAL = PREÇO * COMPRA
DESCONTO = TOTAL - (TOTAL * ((COMPRA / 100) + 0.10)) 
print(f'{TOTAL:.2f}')
print(f'{DESCONTO:.2f}')
