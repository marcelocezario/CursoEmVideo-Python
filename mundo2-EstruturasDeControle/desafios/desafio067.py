'''
Desafios aula 15
Faça um programa que mostre a tabuada de vários números, um de cada vez, ,para cada valor digitado pelo usuário. O
programa será interrompido quando o número solicitado for negativo.
'''
while True:
    numero = int(input('Digite um número que deseja ver a tabuada: '))
    if numero < 0:
        break
    print('='*50)
    print(f'TABUADA DO {numero}'.center(50))
    print('~'*50)
    for i in range(1, 11):
        print(f'{numero} x {i} = {numero * i}')
    print('='*50)
