print('Identificador de palídromo')
frase = str(input('Digite a frase ou palavra de análise: ')).strip().lower()
frase = frase.split()
frase = ''.join(frase)
n = len(frase)
# print(frase)
# print(n)
a = n - 1
cont = 0
for c in range(0, n):
    if frase[c] == frase[a]:
        a = a - 1
        cont = cont + 1
    else:
        c = n
if cont == n:
    print('Frase ou palavra é um Palídromo')
else:
    print('Frase ou palavra não é um Palídromo')