'''
Desafios aula 10
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 por casa km acima do limite.
'''
limiteVelocidade = 80
multaPorKm = 7
velocidadeCarro = int(input('Digite a velocidade do carro: '))
if velocidadeCarro < limiteVelocidade:
    print('Muito bem, continue seguindo as regras de trânsito!')
elif velocidadeCarro == limiteVelocidade:
    print('Você está dentro do limite de velocidade, mas cuidado!')
else:
    print('Você ultrapassou o limite de velocidade, terá que pagar um multa de R$ {:.2f}'.format(multaPorKm*(velocidadeCarro - limiteVelocidade)))
