'''
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leio o nome dos quatro alunos e mostre a ordem sorteada.
'''

import random

aluno1 = str(input('Digite o nome do aluno 1: '))
aluno2 = str(input('Digite o nome do aluno 2: '))
aluno3 = str(input('Digite o nome do aluno 3: '))
aluno4 = str(input('Digite o nome do aluno 4: '))
lista = [aluno1, aluno2, aluno3, aluno4]

random.shuffle(lista)

print('A ordem escolhida foi: {}, {}, {} e {}'.format(lista[0], lista[1], lista[2], lista[3]))
