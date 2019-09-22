print('Soma de números inteiros pares.')
a = 0
for c in range(0,6):
    n = int(input('Digite um número: '))
    if (n % 2) == 0:
        a = a + n
print('A soma dos dos pares é {}' .format(a))