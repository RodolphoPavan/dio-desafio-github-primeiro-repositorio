import match
x = input().split()
n1, n2, n3, n4 = x

N1 = float(n1)
N2 = float(n2)
N3 = float(n3)
N4 = float(n4)
	
media = (N1 + N2 + N3 + N4) / 4
print(f'Media: {media:.1f}')

if media >= 7.0:
    print("Aluno aprovado.")
elif media == 5.0 or media <= 6.9:
    print("Aluno em exame.")
    nota_exame = float(input())
    print(f"Nota do exame: {nota_exame:.1f}")
    media2 = (nota_exame + media)/2
    if media >= 5.0:
        print("Aluno aprovado.")
        print(f'Media final: {media2:.1f}')
    else:
        print( "Aluno reprovado.")
else:
    print( "Aluno reprovado.")



#Media: 5.4
#Aluno em exame.
#Nota do exame: 6.4
#Aluno aprovado.
#Media final: 5.9
