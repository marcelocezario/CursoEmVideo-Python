'''
Desafios aula 14
Faça um programa que leia o sexo de uma pessoa, mas só aceita os valores 'M' ou 'F'. Caso esteja errado, peça a
digitação novamente até ter um valor correto.
'''
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = input('Digite o sexo da pessoa: [M/F] ').strip().upper()
    while sexo != 'M' and sexo != 'F':
        sexo = input('Valor incorreto, digite novamente o sexo da pessoa: [M/F] ').strip().upper()

