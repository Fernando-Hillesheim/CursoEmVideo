x = int(input('Digite um numero:\n'))
for i in range(2,x):
    if(x%i == 0):
        print('Não é primo')
        exit()
print('É primo')