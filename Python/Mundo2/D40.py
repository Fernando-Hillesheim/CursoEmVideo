n1 = float(input('Primeira nota:\n'))
n2 = float(input('Segunda nota:\n'))
media = (n1+n2)/2
if media < 5:
    print('Você foi reprovado com media {}'.format(media))  
elif media >= 7:
    print('Você foi aprovado com media {}'.format(media))
else:
    print('Você esta em recuperação com media {}'.format(media))