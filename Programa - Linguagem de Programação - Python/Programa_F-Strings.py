nome = input('Digite seu nome:')
senha = input ('Qual a sua senha:')
total = 30.5

#Python 3 .format
msg = 'Olá, {}! Sua senha é: {}'.format(nome, senha)
msg2 = 'Total R$ {:.2f}'.format(total)

print(msg)
print(msg2)

#Python 3.6 f-strings
msg = f'Olá, {nome}! Sua senha é: {senha}'
msg2 = f'Total R$ {total:.2f}'

print(msg)
print(msg2)
