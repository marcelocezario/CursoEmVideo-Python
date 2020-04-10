# auto-desafio: exibir todos os número primos abaixo do valor escolhido
numero = int(input('Digite o valor máximo a ser analisado: '))
for i in range(numero, 1, -1):
    primo = True
    for x in range(i-1, 1, -1):
        if i % x == 0:
            primo = False
    if primo:
        print(i)
