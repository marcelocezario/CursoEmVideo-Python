'''
Desafios aula 13
Faça um programa que calcula a soma entre todos os números impares que são múltiplos de três
e que se encontram no intervalo de 1 até 500
'''
s = 0
for i in range (1, 501):
    if i%2 !=0 and i%3 == 0:
        print(i)
        s += i
print(s)
