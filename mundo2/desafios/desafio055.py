'''
Desafios aula 13
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
'''
menor = maior = 0
for c in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if menor == 0 or peso < menor:
        menor = peso
    if maior == 0 or peso > maior:
        maior = peso
print('A pessoa mais leve pesa {}kg e a mais pesada {}kg.'.format(menor, maior))
