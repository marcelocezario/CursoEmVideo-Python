'''
Desafios aula 6
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todos
as informações possíveis sobre ele.
'''
valor = input('Digite algo: ')
print('')
print('É numérico? {}', valor.isnumeric())
print('É alfanumérico? {}', valor.isalnum())
print('É alfabético {}', valor.isalpha())
print('É decimal? {}', valor.isdecimal())
print('É minúsculo? {}', valor.islower())
print('Pode ser impresso? {}', valor.isprintable())
print('É espaço? {}', valor.isspace())
print('É maiúsculo? {}', valor.isupper())
