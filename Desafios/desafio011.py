'''
Desafios aula 7
Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-lo,
sabendo que cada litro de tinta, pinta uma área de 2m²
'''
altura = float(input('Digite a altura da parede em metros: '))
largura = float(input('Digite a largura da parede em metros: '))
area = altura * largura
print('Para pintar essa parede ({}m²), é necessário {} litros de tinta'.format(area, area/2))
