'''
Desafios aula 10
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu
'''
import random

numero = random.randint(1, 5)
opcaoUsuario = int(input('Escolha um número entre 1 e 5 e veja se acerta a escolha do pc: '))
if opcaoUsuario == numero:
    print('Parabéns, você escolheu o mesmo número que o computador!')
else:
    print('O computador escolheu {}, não foi dessa vez!'.format(numero))
