'''
print(5+2)
print(5-2)
print(5*2)
print(5/2)
print(5**2)
print(5//2)
print(5%2)

#potência
print(pow(4, 3))

#raiz quadrada
print(4**(1/2))

#multiplicação de uma string
print('Oi'*5)
print('='*10)

nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {}!'.format((nome)))
print('Prazer em te conhecer {:20}!'.format((nome)))
print('Prazer em te conhecer {:>20}!'.format((nome)))
print('Prazer em te conhecer {:<20}!'.format((nome)))
print('Prazer em te conhecer {:^20}!'.format((nome)))
print('Prazer em te conhecer {:=^20}!'.format((nome)))
'''

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

soma = n1 + n2
multiplicacao = n1 * n2
divisao = n1 / n2
divisaointeira = n1 // n2
potencia = n1 ** n2

print('A soma vale {}, o produto vale {} e a divisão vale {:.3f}'.format(soma, multiplicacao, divisao), end=' ')
print('Divisão inteira {} e potência {}'.format(divisaointeira, potencia))