'''
Desafios aula 12
A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SENIOR
- Acima: MASTER
'''
idade = int(input('Digite a idade do atleta: '))
if idade <= 9:
    categoria = 'MIRIM'
elif idade <= 14:
    categoria = 'INFATIL'
elif idade <= 19:
    categoria = 'JUNIOR'
elif idade <= 20:
    categoria = 'SÊNIOR'
elif idade > 20:
    categoria = 'MASTER'
print('De acordo com a idade informado, a categoria é {}'.format(categoria))
