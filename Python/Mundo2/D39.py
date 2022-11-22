from time import *
from math import trunc
ano = int(input('Qual ano você nasceu?\n'))
agora = time()/(3600*24*365) + 1970
idade = trunc(agora - ano)

