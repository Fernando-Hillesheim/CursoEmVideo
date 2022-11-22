valor = float(input('Valor da casa:\n'))
salario = float(input('Salario:\n'))
anos = int(input('Em quantos anos que pagar?\n'))

mes = valor/(anos * 12)

if salario*0.3 < mes:
    print('Recusado')   

else:
    print('Aprovado')