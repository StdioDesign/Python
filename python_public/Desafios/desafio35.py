print('='*24)
print('Analisador de Triângulos')
print('='*24)
a = int(input('Digite o primeiro comprimento do triângulo: '))
b = int(input('Digite o segundo comprimento do triângulo: '))
c = int(input('Digite o terceiro comprimento do triângulo: '))
if (b - a) < a < (a + b) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
   print('É um triângulo')
else:
  print('Não é um triângulo')

#if (b - a) < a < (a + b):
#    if(a - c) < b < (a + c):
#        if(a - b) < c < (a + b):
#            print('É um triângulo')
#        else:
#           print('Não é um triângulo')
#    else:
#        print('Não é um triângulo')
#else:
#    print('Não é um triângulo')