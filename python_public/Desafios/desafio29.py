v = float(input('Velocidade do carro em Km/h: '))
if v > 80:
    print('Você foi multado em R$ {:.2f}' .format((v - 80)*7))
else:
    print('Carro em velocidade aceitavél.')