'''
Desafias aula 9
Crie um programa que leia o nome completo de uma pessoa e mostre:
* O nome com todas a letras maiúsculas;
* O nome com todas as letras minúsculas;
* Quantas letras ao todo (sem considerar espaços);
* Quantas letras tem o primeiro nome;
'''
nome = str(input('Digite um nome: ')).strip()
print('Nome com todas as letras maiúsculas: {}'.format(nome.upper()))
print('Nome com todas as letras minúsculas: {}'.format(nome.lower()))
print('O nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('O primeiro nome tem {} letras'.format(nome.find(' ')))
