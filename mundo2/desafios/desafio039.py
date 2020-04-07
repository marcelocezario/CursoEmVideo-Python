'''
Desafios aula 12
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
idade = int(input('Digite a idade: '))
idadeAlistar = 18
if idadeAlistar > idade:
    print('Falta {} anos para você se alistar'.format(idadeAlistar-idade))
elif idadeAlistar == idade:
    print('Está na hora de se alistar, procure o exército!')
elif idadeAlistar < idade:
    print('Já se passaram {} anos que você deveria ter se alistado!'.format(idade-idadeAlistar))
