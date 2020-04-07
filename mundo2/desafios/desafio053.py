'''
Desafios aula 13
Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços
'''
frase = str(input('Digite uma frase: ')).strip().upper()
fraseSemEspaco = frase.replace(' ', '')
fraseInvertida = ''
for letra in range(len(fraseSemEspaco)-1, -1, -1):
    fraseInvertida += fraseSemEspaco[letra]
if frase == fraseInvertida:
    print('Essa frase é um palíndromo!')
else:
    print('Essa frase não é um palíndromo!')

print('='*40)
print('Outra opção')
frase = str(input('Digite uma frase: ')).strip().upper().replace(' ', '')
if frase == frase[::-1]:
    print('Essa frase é um palíndromo!')
else:
    print('Essa frase não é um palíndromo!')
