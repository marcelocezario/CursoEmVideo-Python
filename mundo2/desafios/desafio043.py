'''
Desafios aula 12
Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status,
de acordo com a tabela abaixo:
- Abaixo de 18.5: abaixo do peso
- Entre 18.5 e 25: peso ideal
- De 25 até 30: sobrepeso[
- De 30 até 40: obesidade
- Acima de 40: obesidade morbida
'''
altura = int(input('Digite a altura em centimetros (cm): '))
peso = int(input('Digite o peso em quilos (kg): '))
imc = peso / ((altura/100)**2)
if imc < 18.5:
    print('IMC {:.2f}, está abaixo do peso.'.format(imc))
elif imc <= 25:
    print('IMC {:.2f}, está com o peso ideal.'.format(imc))
elif imc < 30:
    print('IMC {:.2f}, está com sobrepeso.'.format(imc))
elif imc < 40:
    print('IMC {:.2f}, está com obesidade.'.format(imc))
elif imc >= 40:
    print('IMC {:.2f}, está com obesidade morbida.'.format(imc))
