x = int(input('Digite um valor\n'))
escolha = int(input('1-binario\n2-octal\n3-hexadecimal'))

bina = bin(x)
octa = oct(x)
hexa = hex(x)

if escolha == 1:
    print(bina)
elif escolha == 2:
    print(octa)
else:
    print(hexa)