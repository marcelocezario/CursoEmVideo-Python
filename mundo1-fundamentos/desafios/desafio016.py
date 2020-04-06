'''
Desafios aula 8
Crie um programa que leia um número Real qualquer pelo teclado emostre na tela a sua porção inteira.
Ex: digite um número: 6.127. O número 6.127 tem parte Inteira 6
'''
import math
num = float(input('Digite um número real qualquer (float): '))
inteira = math.trunc(num);
print('A porção inteira de {} é {}'.format(num, inteira))
