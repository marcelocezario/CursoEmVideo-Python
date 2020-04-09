'''
Desafios aula 14
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em mum número entre 0 e 10. Só que agora o jogador vai
tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''
from random import randint
palpites = 0
vencedor = False
while vencedor != True:
    numero = randint(1, 10)
    palpites += 1
    opcaoUsuario = int(input('Escolha um número entre 1 e 10 e veja se acerta a escolha do pc: '))
    if opcaoUsuario == numero:
        print('Parabéns, você escolheu o mesmo número que o computador na {}ª tentativas!'.format(palpites))
        vencedor = True
    else:
        print('O computador escolheu {}, não foi dessa vez!'.format(numero))
        print('Tente novamente!!')
