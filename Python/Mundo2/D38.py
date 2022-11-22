x = int(input('n1:\n'))
y = int(input('n2:\n'))

if x == y:
    print('iguais')
elif x > y:
    print('{} é maior que {}'.format(x,y))
else:
    print('{}>{}'.format(y,x))