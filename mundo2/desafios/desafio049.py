'''
Desafios aula 13
Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora
utilizando um laço for
'''
numero = int(input('Escolha um número: '))
for c in range (1, 11):
    print('{} x {} = {}'.format(numero, c, numero*c))
