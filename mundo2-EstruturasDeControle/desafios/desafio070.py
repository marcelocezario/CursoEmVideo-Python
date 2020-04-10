'''
Desafios aula 15
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
a) qual é o total gasto na compra.
b) quantos produtos custam mais de R$ 1000,00
c) qual é o nome do produto mais barato
'''
total = 0
acima1000 = 0
produtoMaisBarato = ''
menorPreco = 0
while True:
    produto = str(input('Digite o nome do produto: ')).strip()
    preco = float(input('Digite o preço do produto: '))
    total += preco
    if preco > 1000:
        acima1000 += 1
    if produtoMaisBarato == '' or menorPreco > preco:
        produtoMaisBarato = produto
        menorPreco = preco
    opcao = input('Deseja continuar? [S/N] ').strip().upper()[0]
    while opcao not in 'SN':
        opcao = input('Opção inválida. Deseja continuar? [S/N] ').strip().upper()[0]
    if opcao == 'N':
        break
print(f'O total gasto foi de R$ {total:.2f}')
print(f'Ao todo, teve {acima1000} produtos acima de R$ 1000.00.')
print(f'O produto mais barato foi {produtoMaisBarato} que custou R$ {menorPreco:.2f}.')
