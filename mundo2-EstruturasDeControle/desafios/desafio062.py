'''
Desafios aula 14
Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele
disse que quer mostrar 0 termos.
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
opcao = int(input('Deseja mostrar mais quantos termos? [digite 0 para finalizar] '))
while opcao != 0:
    cont = 1
    while cont <= opcao:
        print(f'{termo}', end=' → ')
        termo += razao
        cont += 1
    print('Acabou!')
    opcao = int(input('Deseja mostrar mais quantos termos? [digite 0 para finalizar] '))
print('Obrigado por utilizar o programa!')
