'''
Desafios aula

'''
preco = float(input('Digite o preço do produto: '))
descontoPorCento = 5

print('O valor do produto com {}% de desconto é {:.2f}'
      .format(descontoPorCento,preco*(100-descontoPorCento)/100))
