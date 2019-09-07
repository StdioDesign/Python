ano = int(input('Digite o ano desejado: '))
if ano % 4 == 0 :
    if ano % 400 == 0:
        print('Ano não bissexto')
    else:
        if ano % 100 != 0:
            print('Ano bissexto')
else:
    print('Ano não bissexto')