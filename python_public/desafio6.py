cont = 0
soma = 0
while True:
    idade = float(input('Digite uma idade ou -1 para finalizar: '))
    if idade == -1:
        break
    else:
       cont += 1
       soma += idade
print(f'A média das idades escritas foram de {soma/cont:.2f} ')
