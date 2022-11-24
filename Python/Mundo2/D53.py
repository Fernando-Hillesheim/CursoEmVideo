x = str(input('Digite uma frase:\n'))
x = x.replace(" ", "")
y = x[::-1]
if y == x:
    print('É palindromo')
else:
    print('Não é palindromo')