'''
Desafios aula 12
Elabore um prograna que calcule o valor a ser por um produto, considerando o seu preço normal
e condição de pagamento:
- a vista dinheiro/cheque: 10% desconto
- a vista no cartão: 5% de desconto
- em 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
'''
preco = float(input('Digite o preço do produto: '))
valorParcela = preco
formaPagamento = int(input('Qual a forma de pagamento?\n'
                           '1 - dinheiro (desconto de 10%)\n'
                           '2 - cheque (desconto de 10%)\n'
                           '3 - cartão (em até 3 parcelas)\n'))
if formaPagamento == 1 or formaPagamento == 2:
    valorParcela = preco * 0.9
    prazo = 1
elif formaPagamento == 3:
    prazo = int(input('Qual o prazo desejado?\n'
          '1 - a vista com 5% de desconto\n'
          '2 - 2 parcelas sem desconto\n'
          '3 - 3 parcelas com acréscimo de 20%\n'))
    if prazo == 1:
        valorParcela = preco * 0.95
    elif prazo == 2:
        valorParcela = preco / 2
    elif prazo == 3:
        valorParcela = (preco * 1.2) / 3
print('O pagamento será',
      'à vista,'if prazo==1 else 'em {} parcelas'.format(prazo),
      'no valor de R$ {:.2f}.'.format(valorParcela))
