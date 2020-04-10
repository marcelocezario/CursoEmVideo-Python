'''
Desafios aula 13
Faça uma programa que mostre na tela uma contagem regressiva para o estouro dos fogos de
artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
'''
from emoji import emojize
from time import sleep
print('Contagem regressiva!!')
for c in range (10, 0, -1):
    print(c)
    sleep(1)
print(emojize(":clock12:Feliz ano novo!!:fireworks:",use_aliases=True))