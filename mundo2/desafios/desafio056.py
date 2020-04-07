'''
Desafios aula 13
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
*A média de idade do grupo;
*Qual é o nome do homem mais velho;
*Quantas mulheres têm menos de 20 anos.
'''
somaIdades = 0
homemMaisVelho = ''
idadeHomemMaisVelho = 0
mulheresAcima20Anos = 0
for c in range(1, 5):
    nome = input('Digite o nome da {}ª pessoa: '.format(c))
    idade = int(input('Digite a idade da {}ª pessoa: '.format(c)))
    genero = input('Digite o genero da {}ª pessoa (M/F): '.format(c)).strip().upper()
    somaIdades += idade
    if genero == 'M':
        if idadeHomemMaisVelho == 0 or idadeHomemMaisVelho < idade:
            homemMaisVelho = nome
            idadeHomemMaisVelho = idade
    elif genero == 'F':
        if idade >= 20:
            mulheresAcima20Anos += 1
print('A média de idade é {}.'.format(somaIdades/4))
if homemMaisVelho == '':
    print('Não foi adicionando nenhum homem a lista.')
else:
    print('O homem mais velho é o {} que possui {} anos.'.format(homemMaisVelho, idadeHomemMaisVelho))
if mulheresAcima20Anos == 0:
    print('Não foi adicionado nenhuma mulher com 20 anos ou mais na lista.')
else:
    print('A lista possui {} mulheres com mais de 20 anos'.format(mulheresAcima20Anos))
