'''
Desafios aula 10
Faça um programa que leia três números e mostre qual é o maior e qual é o menor
'''
numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
numero3 = int(input('Digite mais um número: '))
if numero1 >= numero2 and numero1 >= numero3:
    maior = numero1
elif numero2 >= numero1 and numero2 >= numero3:
    maior = numero2
elif numero3 >= numero1 and numero3 >= numero2:
    maior = numero3
if numero1 <= numero2 and numero1 <= numero3:
    menor = numero1
elif numero2 <= numero1 and numero2 <= numero3:
    menor = numero2
elif numero3 <= numero1 and numero3 <= numero2:
    menor = numero3
print('O maior número é o {} e o menor é o {}'.format(maior, menor))
