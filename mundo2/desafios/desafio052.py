'''
Desafios aula 13
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''
numero = int(input('Digite um número para saber se ele é primo: '))
primo = True
for i in range(numero-1, 1, -1):
    if numero % i == 0:
        primo = False
if primo:
    print('{} é um número primo!'.format(numero))
else:
    print('{} não é um número primo!'.format(numero))
