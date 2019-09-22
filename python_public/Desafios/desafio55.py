print('Leitor de pesos!')

pmaior = 0
pmenor = 0

for c in range(0, 5):
    p = int(input('Digite o Peso: '))
    if pmaior < p:
        pmaior = p
    if pmenor == 0:
        pmenor = pmaior
    elif pmenor > p:
        pmenor = p

print('O maior peso é {}' .format(pmaior))
print('O menor peso é {} ' .format(pmenor) )