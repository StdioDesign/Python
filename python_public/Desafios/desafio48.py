print('Soma de numeros impares que são multiplos de três')
n = 0
for c in range(0, 500+1, 3):
    n = c + n
print(n)
# ----------------------------------------------------
n = 0
for c in range(0, 500, 1):
    if (c % 3) == 0:
        n = c + n
print(n)