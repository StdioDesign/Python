n = int(input('Digite um valor e veja seu fatorial: '))
fat = 1
for i in range(n, 0, -1):
    fat *= i
print(f'O fatorial de {n} é igual a {fat}')