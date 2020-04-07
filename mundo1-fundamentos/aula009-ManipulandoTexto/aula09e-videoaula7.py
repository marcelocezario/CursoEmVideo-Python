nome = input('Qual é o seu nome: ')
print('Prazer em te conhecer {}!'.format(nome))
print('Prazer em te conhecer {:20}!'.format(nome))
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))


print("""
Qual é o seu nome: marcelo
Prazer em te conhecer marcelo!
Prazer em te conhecer marcelo             !
Prazer em te conhecer              marcelo!
Prazer em te conhecer marcelo             !
Prazer em te conhecer       marcelo       !
Prazer em te conhecer ======marcelo=======!
""")