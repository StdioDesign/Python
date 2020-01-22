peso = []
cont = 0
for i in range(1, 8):
    p = float(input(f'Digite o peso da pessoa {i}: '))
    peso.append(p)
    media = sum(peso)/i
    if p >= 90:
        cont +=1

print(f'{cont} pessoas com mais de 90kg!')
print(f'A media dos pesos são de {media:.2f}kg')