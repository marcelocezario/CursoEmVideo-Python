'''
Desafias aula 9
Faça um programa que leio um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
'''
numero = int(input('Digite um número de 0 a 9999: '))
calculo = str(10000+numero)
unidade = calculo[4]
dezena = calculo[3]
centena = calculo[2]
milhar = calculo[1]
print('Unidade {}'.format(unidade))
print('Dezena {}'.format(dezena))
print('Centena {}'.format(centena))
print('Milhar {}'.format(milhar))
