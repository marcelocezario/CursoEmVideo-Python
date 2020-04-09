'''
Desafios aula 14
Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicictada em cada caso.
'''

opcao = 0
while opcao != 5:
    valor1 = int(input('Digite o primeiro valor: '))
    valor2 = int(input('Digite o segundo valor: '))
    print('|{:<50}|\n|{:<50}|\n|{:<50}|\n|{:<50}|\n|{:<50}|\n|{:<50}|\n|{:<50}|'
          .format('=' * 50, '[1]somar', '[2]multiplicar', '[3]maior', '[4]novos números', '[5]sair do programa',
                  '=' * 50))
    opcao = int(input('Qual a opção deseja? '))
    if opcao == 1:
        print('{} + {} = {}'.format(valor1, valor2, valor1 + valor2))
        if input('Deseja continuar? [S/N] ').strip().upper() == 'N':
            opcao = 5
    elif opcao == 2:
        print('{} x {} = {}'.format(valor1, valor2, valor1 * valor2))
        if input('Deseja continuar? [S/N] ').strip().upper() == 'N':
            opcao = 5
    elif opcao == 3:
        if valor1 > valor2:
            print('O maior valor é {}.'.format(valor1))
        else:
            print('O maior valor é {}.'.format(valor2))
        if input('Deseja continuar? [S/N] ').strip().upper() == 'N':
            opcao = 5
    elif opcao != 4 and opcao != 5:
        print('Opção inválida, por favor tente novamente!')
