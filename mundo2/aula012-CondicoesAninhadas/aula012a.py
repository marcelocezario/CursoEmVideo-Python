nome = str(input('Qual é o seu nome? '))
if nome == 'Marcelo':
    print('Que nome bonito!')
elif nome == 'Pedro':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cládia Jéssica Juliana':
    print('Belo nome feminio!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}'.format(nome))
