2#transformação string
frase = 'Curso em Vídeo Python'

substituirString = frase.replace('Python', 'Android')
print(substituirString)
print()

deixarMaiuscula = frase.upper()
print(deixarMaiuscula)
deixaMinuscula = frase.lower()
print(deixaMinuscula)
print()

primeiraMaiusculaFrase = frase.capitalize()
print(primeiraMaiusculaFrase)
print()

primeiraMaiusculaPalavras = frase.title()
print(primeiraMaiusculaPalavras)
print()

frase = '   Aprenda Python  '
print(frase)
removerEspacos = frase.strip()
print(removerEspacos)
print()

removerEspacosDireita = frase.rstrip()
print(removerEspacosDireita)
removerEspacosEsquerda = frase.lstrip()
print(removerEspacosEsquerda)