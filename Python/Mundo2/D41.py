from time import *
from math import trunc
ano = int(input('Qual ano você nasceu?\n'))
agora = time()/(3600*24*365) + 1970
idade = trunc(agora - ano)

if idade < 9:
    print('Mirim')
elif idade < 14:
    print('Infantil')
elif idade < 19:
    print('Junior')
elif idade < 20:
    print('Senior')
else:
    print('Master')