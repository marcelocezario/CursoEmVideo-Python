'''
Desafios aula 10
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
Para salários inferiores ou iguais, o aumento é de 15%.
'''
salario = float(input('Digite qual o valor atual do salário: '))
if salario>1250:
    novoSalario = salario * 1.1
else:
    novoSalario = salario * 1.15
print('O novo salário é de R$ {:.2f}'.format(novoSalario))
