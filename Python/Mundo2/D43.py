peso = float(input('Qual seu peso?\n'))
altura = float(input('Qual sua altura?\n'))

imc = peso/(altura**2)

if imc < 18.5:
    print('Abaixo do peso, imc = {}'.format(imc))
elif imc < 25:
    print('Peso ideal, imc = {}'.format(imc))
elif imc < 30:
    print('Sobrepeso, imc = {}'.format(imc))
elif imc < 40:
    print('Obeso, imc = {}'.format(imc))
else:
    print('Planeta, imc = {}'.format(imc))



























