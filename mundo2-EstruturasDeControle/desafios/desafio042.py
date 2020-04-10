'''
Desafios aula 12
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de
triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
'''
r1 = float(input('Digite a medida da primeira reta: '))
r2 = float(input('Digite a medida da segunda reta: '))
r3 = float(input('Digite a medida da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas acima podem formar um triângulo')
    if r1 == r2 == r3:
        print('O triângulo formado será Equilátero!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('O triângulo formado será Isósceles!')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('O triângulo formado será Escaleno!')
else:
    print('As retas acima não podem formar um triângulo')

