'''
Desafios aula 12
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos
ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
ou então o empréstimo será negado.
'''
valor = float(input('Qual o valor do imóvel? '))
salario = float(input('Qual o salário? '))
prazoEmAnos = int(input('Qual o prazo escolhido em anos? '))
parcela = valor / (prazoEmAnos * 12)
if (parcela > salario * 0.3):
    print('O empréstimo foi negado!')
elif (parcela <= salario * 0.3):
    print('O empréstimo foi aprovado, valor mensal da parcelo é R$ {:.2f}'.format(parcela))
