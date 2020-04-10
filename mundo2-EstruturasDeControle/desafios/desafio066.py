'''
Desafios aula 15
Crie um programa  que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
valor 999, que é a condição de parada. No final, mostre quantos número foram digitados e qual foi a soma entre eles
(desconsiderando o flag)
'''
soma = 0
cont = 0
while True:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    soma += numero
    cont += 1
print(f'Foram digitado {cont} números, soma total de {soma}.')
