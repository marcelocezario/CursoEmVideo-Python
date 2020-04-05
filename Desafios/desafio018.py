import math

angulo = int(input('Digite um angulo qualquer: '))

seno = math.sin(math.radians(angulo))
consseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O seno do angulo de {}º é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(angulo, seno, consseno, tangente))