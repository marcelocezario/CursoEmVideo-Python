'''
Desafias aula 8
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
'''
import random
aluno1 = str(input('Digite o nome do aluno 1: '))
aluno2 = str(input('Digite o nome do aluno 2: '))
aluno3 = str(input('Digite o nome do aluno 3: '))
aluno4 = str(input('Digite o nome do aluno 4: '))
lista = [aluno1, aluno2, aluno3, aluno4]
alunoEscolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(alunoEscolhido))
