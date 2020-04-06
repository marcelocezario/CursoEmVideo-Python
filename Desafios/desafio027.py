'''
Faça um programa que leia o nome completo de um pessoa,
mostrando em seguida o primeiro e o último nome separadamente.
'''
nome = input('Digite o nome completo: ')

nomeSeparado = nome.split()

print('Primeiro nome: {}'.format(nomeSeparado[0]))
print('Último nome: {}'.format(nomeSeparado[-1]))
