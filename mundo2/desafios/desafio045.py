'''
Desafios aula 12
Crie um programa que faça o computador jogar Jokenpô com você
'''
import random
opcao = int(input('Escolha uma opcao abaixo:\n'
                  '1 - pedra\n'
                  '2 - papel\n'
                  '3 - tesoura\n'
                  'Qual a sua opção? '))
opcaoPc = random.randint(1, 3)
if opcao == 1:
    if opcaoPc == 1:
        print('O computador também escolheu pedra, empate!')
    elif opcaoPc == 2:
        print('O computador escolheu papel, você perdeu!')
    elif opcaoPc == 3:
        print('O computador escolheu tesoura, você venceu!')
elif opcao == 2:
    if opcaoPc == 1:
        print('O computador escolheu pedra, você venceu!')
    elif opcaoPc == 2:
        print('O computador também escolheu papel, empate!')
    elif opcaoPc == 3:
        print('O computador escolheu tesoura, você perdeu!')
elif opcao == 3:
    if opcaoPc == 1:
        print('O computador escolheu pedra, você perdeu!')
    elif opcaoPc == 2:
        print('O computador escolheu papel, você venceu!')
    elif opcaoPc == 3:
        print('O computador também escolheu tesoura, empate!')
