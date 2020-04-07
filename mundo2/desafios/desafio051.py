'''
Desafios aula 13
Desenvolva um programa que leia o primeiro termo e a razão de uma PA (progressão aritmética).
No final, mostre os 10 primeiro termos dessa progressão.
'''
primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite qual a razão da PA: '))
for i in range(primeiro, primeiro+(razao * 10), razao):
    print('{}'.format(i), end=' → ')
print('FIM')
