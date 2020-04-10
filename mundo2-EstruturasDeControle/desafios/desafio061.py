'''
Desafios aula 14
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiro termos da progressão usando a
estrutura while.
'''
primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite qual a razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo}', end=' → ')
    termo += razao
    cont += 1
print('Acabou!')
