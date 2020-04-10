'''
Desafios aula 14
Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequencia de
Fibonacci.
Ex: 0 → 1 → 1 → 2 → 3 → 5 → 8
'''
titulo = 'SEQUENCIA DE FIBONACCI'
print('='*50)
print(f'{titulo:^50}')
print('='*50)
qtde = int(input('Digite a quantidade de números da sequência de Fibonacci que deseja exibir: '))
cont = 1
termo0 = 0
termo1 = 1
termo2 = 1
while cont <= qtde:
    print(f'{termo0}', end=' → ')
    termo0 = termo1
    termo1 = termo2
    termo2 = termo0 + termo1
    cont += 1
print('FIM')
