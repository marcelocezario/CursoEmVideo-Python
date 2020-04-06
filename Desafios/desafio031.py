'''
Desafios aula 10
Desenvolva um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200km e R$ 0,45
viagens mais longas
'''
distancia = int(input('Digite a distância da viagem: '))
if distancia <= 200:
    valorKm = 0.50
else:
    valorKm = 0.45
print('O valor da passagem é R$ {:.2f}'.format(distancia * valorKm))
