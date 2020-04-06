#análise string
frase = 'Curso em Vídeo Python'

comprimentoString = len(frase)
print(comprimentoString)
print()

contarStringEspecifica = frase.count('o')
print(contarStringEspecifica)
print(frase.count('o', 0, 13))
print()

procurarStringEspecifica = frase.find('deo')
print(procurarStringEspecifica)
print(frase[procurarStringEspecifica:])
print()

print('Curso' in frase)
print('Marcelo' in frase)
print()



