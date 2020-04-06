'''
Desafias aula 9
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
'''
cidade = input('Digite o nome de uma cidade: ').upper().strip()
print('Cidade começa com a palavra "SANTO"?', 'SANTO' in cidade[:5])
