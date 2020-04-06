nome = 'Marcelo'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7:30m'}

print('Olá! Muito em prazer em te conhecer, {}{}{}!!'.format(cores['amarelo'], nome, cores['limpa']))
