'''
Desafios aula 10
Crie um programa que leia um número inteiro qualquer, e mostre na tela se ele é par ou impar.
'''
numero = int(input('Digite um número inteiro qualquer: '))
resto = numero % 2
print('O número é par!'if resto == 0 else 'O número é impar')
