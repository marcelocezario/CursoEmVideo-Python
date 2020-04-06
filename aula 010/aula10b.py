nome = str(input('Qual o seu nome? '))
#condicional simples
if nome == 'Marcelo':
    print('Que legal, o meu também')
print('Bom dia, {}'.format(nome))
print('')

#condicional composta
nome = str(input('Qual o seu nome? '))
if nome == 'Marcelo':
    print('Que legal, o meu também')
else:
    print('O meu é Marcelo')
print('Bom dia, {}'.format(nome))
