from random import *

opcoes = ['Pedra', 'Papel', 'Tesoura']

opcao = choice(opcoes)

escolha = str(input('Digite Pedra, Papel ou Tesoura\n'))

if opcao == escolha:
    print('Empate')
elif opcao == 'Pedra' and escolha == 'Papel':
    print('You Win')
elif opcao == 'Pedra' and escolha == 'Tesoura':
    print('PC Win')
elif opcao == 'Papel' and escolha == 'Tesoura':
    print('You Win')
elif opcao == 'Papel' and escolha == 'Pedra':
    print('PC Win')
elif opcao == 'Tesoura' and escolha == 'Tesoura':
    print('You Win')    
else:
    print('PC Win')