'''
Desafios aula 15
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o
usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
'''
maiores = 0
homens = 0
mulheres = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo: [M/F] ')).strip().upper()[0]
#    while sexo != 'M' and sexo != 'F':
    while sexo not in 'MF':
        sexo = str(input('Valor inválido! Digite novamente o sexo: [M/F] ')).strip().upper()
    if idade >= 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    opcao = input('Deseja continuar? [S/N] ').strip().upper()[0]
#    while opcao != 'S' and opcao != 'N':
    while opcao not in 'SN':
        opcao = str(input('Valor inválido! Deseja continuar? [S/N] ')).strip().upper()
    if opcao == 'N':
        break
print(f'O total de pessoas com 18 anos ou mais é: {maiores}.')
print(f'Foram cadastrados um total de {homens} homens.')
print(f'E um total de {mulheres} mulher com menos de 20 anos.')
