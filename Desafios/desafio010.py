'''
Desafios aula 7
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
quantos dólares ela pode comprar.
'''
valorCarteira = float(input('Digite quanto dinheiro possui na carteira: '))
dolar = 3.27
print('Com seu dinheiro em carteira, é possível comprar US$ {:.2f}'.format(valorCarteira/dolar))
