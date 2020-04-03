import math

angulo = int(input('Digite um angulo qualquer: '))

seno = math.sin(angulo)
consseno = math.cos(angulo)
tangente = math.tan(angulo)

print('O seno do angulo de {}º é {}, o cosseno é {} e a tangente é {}'.format(angulo, seno, consseno, tangente))