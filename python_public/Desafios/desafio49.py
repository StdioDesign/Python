print('TABUADA')
n = int(input('Digite um número: '))
for c in range(0, 10+1):
    a = n*c
    print('{} * {} = {}'.format(n, c, a))
print('FIM')