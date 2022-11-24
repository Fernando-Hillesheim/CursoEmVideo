from datetime import date

maior = 0
menor = 0
atual = date.today().year
for i in range(7):
    x = int(input('Que ano voce nasceu?\n'))
    if atual - x > 18:
        maior += 1
    else:
        menor += 1
print('Maior = {}\nMenor = {}'.format(maior,menor))
