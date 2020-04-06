import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz quadrada de {} é {}'.format(num, raiz))
print('O valor arrendondado para cima da raiz quadrada de {} é {}'.format(num, math.ceil(raiz)))
print('O valor arrendondado para baixo da raiz quadrada de {} é {}'.format(num, math.floor(raiz)))