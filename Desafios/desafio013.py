'''
Desafios aula 7
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
'''
salario = float(input('Digite o salário do funcionário: '))
porcentagemAumento = 15
print('O novo salário com aumento de {}% é de R$ {:.2f}'
      .format(porcentagemAumento, salario*(1+porcentagemAumento/100)))
