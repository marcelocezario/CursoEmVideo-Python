'''
Desafios aula 7
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
que o carro custa R$60 por dia e R$0,15 por Km rodado.
'''
km = int(input('Digite a quantidade de km percorridos: '))
dias = int(input('Digite a quantidade de dias: '))
valorAluguel = km*0.15 + dias*60
print('O valor total do aluguel é R$ {}.'.format(valorAluguel))
