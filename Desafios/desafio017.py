from math import hypot

catetoOposto = float(input('Digite qual o cateto oposto: '))
catetoAdjacente = float(input('Digite qual o cateto adjacente: '))
hipotenusa = hypot(catetoAdjacente, catetoOposto)

print('A hipotenusa é {}'.format(hipotenusa))
