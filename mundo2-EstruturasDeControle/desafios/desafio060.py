'''
Desafios aula 14
Faça um programa que leia um número qualquer e mostre o seu fatorial.
'''
numero = int(input('Digite um número qualquer: '))
fatorial = numero
print(f'{numero}! = ', end='')
while numero != 1:
    print(f'{numero}', end=' x ')
    numero -= 1
    fatorial = fatorial * numero
    if numero == 1:
        print(f'1 = {fatorial}')
