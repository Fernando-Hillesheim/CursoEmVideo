maior = 0.0
menor = 0.0
key = True

for i in range(5):
    peso = float(input('Qual seu peso?\n'))
    if peso > maior:
        maior = peso
    if key == True:
        menor = peso
        key = False
    else:
        if peso < menor:
            menor = peso

print('Menor = {}\nMaior = {}'.format(menor, maior))