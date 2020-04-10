'''
Desafios aula 12
Escreva um programa que leia um número inteiro qualquer e peça para o usuário
escolher qual será a base de conversão:
1 - para binário
2 - para octal
3 - para hexadecimal
'''
numero = int(input('Digite um número inteiro: '))
opcao = int(input('Escolha uma opção abaixo:\n'
                  '1 - converter número para binário\n'
                  '2 - converter número para octal\n'
                  '3 - converter número para hexadecimal\n'
                  'Qual a sua escolha? '))
if (opcao == 1):
    nrConvertido = bin(numero)
    print('O número {} convertido para binário é: {}'.format(numero, nrConvertido[2:]))
elif (opcao == 2):
    nrConvertido = oct(numero)
    print('O número {} convertido para octal é: {}'.format(numero, nrConvertido[2:]))
elif (opcao ==3):
    nrConvertido = hex(numero)
    print('O número {} convertido para hexadecimal é: {}'.format(numero, nrConvertido[2:]))
