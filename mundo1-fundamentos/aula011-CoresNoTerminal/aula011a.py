'''
Style = 0-none / 1-bold / 4-underline / 5-negativo
Text = 30 / 31 / 32 / 33 / 34 / 35 / 36 / 37
Back = 40 / 41 / 42 / 43 / 44 / 45 / 46 / 47
'''
print('\033[4;30;45mOlá, Mundo!\033[m')

a = 3
b = 5
print('Os valores são \033[32m{} e \33[31m{}'.format(a, b))

nome = 'Marcelo'
print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format('\033[4;34m', nome, '\033[m'))
