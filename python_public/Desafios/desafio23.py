n = int(input('Digite um número de 0 a 9999: '))
# print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}' .format(n[3], n[2], n[1], n[0]))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}' .format(u, d, c, m))
