from datetime import date
atual = date.today().year
ano = int(input('Digite o ano de nasciemento: '))
idade = atual - ano
print('O atleta tem {} anos'.format(idade))

if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <=20:
    print('SENIOR')
elif idade >=21:
    print('MASTER')