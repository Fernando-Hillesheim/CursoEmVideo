pessoas = []
mulheres = []
media = 0

for i in range(4):
    pessoa = {}
    x = input('Qual seu nome?\n')
    pessoa['nome'] = x
    x = int(input('Qual sua idade?\n'))
    pessoa['idade'] = x
    media += x
    x = input('Qual seu sexo?\n')
    pessoa['sexo'] = x
    if x == 'f': mulheres.append(pessoa)
    pessoas.append(pessoa)


media = media/4
maior = 0
mais_velho = ""
for i in pessoas:
    if i['sexo'] == 'm' and i['idade'] > maior:
        maior = i['idade']
        mais_velho = i['nome']

print('O homem mais velho é {} com {} anos'.format(mais_velho, maior))

print('Mulheres com menos de 20 anos:')
for i in mulheres:
    if i['idade'] < 20:
        print(i['nome'])