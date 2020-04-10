'''
Desafios aula 15
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando
o total de vitórias consecutivas que ele conquistou no final do jogo
'''
from random import randint
vitorias = 0
while True:
    opcao = input('Par ou Ímpar? [P/I] ').strip().upper()
    numero = int(input('Escolha um número: '))
    computador = randint(1, 10)
    print(f'O computador jogou {computador}!')
    if (numero + computador) % 2 == 0:
        if opcao == 'P':
            vitorias += 1
            print('Parabéns, você venceu!!')
        else:
            break
    else:
        if opcao == 'I':
            vitorias += 1
            print('Parabéns, você venceu!!')
        else:
            break
print(f'Você perdeu!! Você teve ao todo {vitorias} consecutivas!')
