'''
Desafios aula 13
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
a maioridade e quantas já são maiores.
'''
import datetime
maiores = 0
menores = 0
for i in range(0, 7):
    ano = int(input('Digite o ano de nascimento: '))
    if (datetime.date.today().year - ano) >= 21:
        maiores += 1
    else:
        menores += 1
print('{} pessoas atingiram a maioridade.'.format(maiores))
print('{} pessoas não atingiram a maioridade.'.format(menores))
