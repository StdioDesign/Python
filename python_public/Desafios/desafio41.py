from datetime import date

print('Confederação Nacional de Natação')
ano = int(input('Digite seu ano de nascimento: '))

data = date.today()
idade = data.year - ano

if idade < 10:
    print('Categoria MIRIM')
elif 9 < idade < 15:
    print('Categoria INFANTIL')
elif 14 < idade < 20:
    print('Categoria JUNIOR')
elif 19 < idade < 21:
    print('Categoria SÊNIOR')
else:
    print('Categoria MASTER')