'''
Desafios aula 13
Desenvolva um programa que leia seis números inteiros e mostra a soma apenas daqueles que forem
pares. Se o valor digitado for impar, desconsidere-o.
'''
soma = 0
for i in range(0, 6):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        soma += numero
print('A soma dos números pares é {}'.format(soma))
