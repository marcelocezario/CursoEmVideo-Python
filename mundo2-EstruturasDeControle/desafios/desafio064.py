'''
Desafios aula 14
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor
999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag)
'''
cont = 0
soma = 0
numero = 0
while numero != 999:
    numero = int(input('Digite um número: '))
    if numero != 999:
        cont += 1
        soma += numero
print(f'Foram digitados {cont} números, e a soma deles é {soma}.')
