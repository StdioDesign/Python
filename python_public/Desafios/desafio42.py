print('='*24)
print('Analisador de Triângulos')
print('='*24)
a = int(input('Digite o primeiro comprimento do triângulo: '))
b = int(input('Digite o segundo comprimento do triângulo: '))
c = int(input('Digite o terceiro comprimento do triângulo: '))
if (b - a) < a < (a + b) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
   if a == b == c:
       print('Triãngulo Equilátero')
   elif (a == b and b != c) or (a == c and c != b) or (c == b and b != a):
       print('Triângulo Isóceles')
   elif a != b != c:
       print('Triângulo Escaleno')
else:
  print('Não é um triângulo')