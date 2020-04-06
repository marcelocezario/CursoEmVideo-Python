from math import sqrt, ceil, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz quadrada de {} é {}'.format(num, raiz))
print('O valor arrendondado para cima da raiz quadrada de {} é {}'.format(num, ceil(raiz)))
print('O valor arrendondado para baixo da raiz quadrada de {} é {}'.format(num, floor(raiz)))