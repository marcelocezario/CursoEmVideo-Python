'''
Desafios aula 8
Faça um program que leia o comprimento do cateto oposto e do cateto adjacente
de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
'''
from math import hypot
catetoOposto = float(input('Digite qual o cateto oposto: '))
catetoAdjacente = float(input('Digite qual o cateto adjacente: '))
hipotenusa = hypot(catetoAdjacente, catetoOposto)
print('A hipotenusa é {}'.format(hipotenusa))
