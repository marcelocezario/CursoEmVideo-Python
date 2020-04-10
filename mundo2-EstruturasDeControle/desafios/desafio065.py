'''
Desafios aula 14
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
a digita valores
'''
soma = 0
cont = 0
maior = menor = ''
opcao = ''
while opcao != 'N':
    numero = int(input('Digite um número: '))
    soma += numero
    cont += 1
    if (maior == '' or maior < numero):
        maior = numero
    if (menor == '' or menor > numero):
        menor = numero
    opcao = str(input('Deseja continuar a execução? [S/N] ').strip().upper())
    while opcao != 'S' and opcao != 'N':
        opcao = str(input('Opção inválida! Deseja continuar a execução? [S/N] ').strip().upper())
print(f'Ao todo foram digitados {cont} números, a soma entre eles é {soma} dando assim uma média de {(soma/cont):.2f}')
print(f'O menor valor lido foi {menor} e o maior foi {maior}.')
