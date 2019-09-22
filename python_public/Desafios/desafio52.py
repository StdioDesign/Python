print('Identificador de números primos')
n = int(input('Digite um número: '))
a = 0
for c in range(n, 0, -1):
    if n % c == 0:
        a = a + 1
if a > 2:
    print('Não é primo!')
else:
    print('É primo!')