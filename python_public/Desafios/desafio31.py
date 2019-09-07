k = int(input('Qual a distância em Km a ser percorrida? '))
if k <= 200:
    print('Sua viajem custará: R$ {:.2f}' .format(k*0.50))
else:
    print('Sua viajem custará: R$ {:.2f}' .format(k*0.45))