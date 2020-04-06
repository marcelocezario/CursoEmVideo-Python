'''
Desafias aula 9
Faça um programa que leia uma frase pelo tedclado e mostre:
*Quantas vezes aparece a letra "A"
*Em que posição ela aparece pela primeira vez?
*Em que posição ela aparece pela última vez?
'''
frase = input('Digite uma frase: ').upper()
qtde = frase.count('A')
primeira = frase.find('A')
ultima = frase.rfind('A')
print('Quantidade de lestras "A": {}'.format(qtde))
print('Primeira posição que aparece: {}'.format(primeira))
print('Ultima posição que aparece: {}'.format(ultima))
