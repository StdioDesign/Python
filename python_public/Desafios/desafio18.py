from math import cos, sin, tan, radians
n = float(input('Digite o ângulo: '))
print('Seu seno é {:.2f}\nSeu cosseno é {:.2f}\nSua tangente é {:.2f}' .format(sin(radians(n)), cos(radians(n)), tan(radians(n))))