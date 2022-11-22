from time import *
from math import trunc
ano = int(input('Qual ano você nasceu?\n'))
agora = time()/(3600*24*365) + 1970
idade = trunc(agora - ano)
aux = idade - 18

if aux == 0:
    print('Você deve se alistar esse ano')
elif aux < 0:
    print('Você deve se alistar daqui a {} anos'.format(-1*aux))
else:
    print('Você devia ter se alistado há {} anos'.format(aux))

    
#poderia ser usado o date.today().year
#obtido atraves do import: from datetime import date
