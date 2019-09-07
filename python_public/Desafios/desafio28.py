import random

print('O computador escolherá um número ente 0 e 5')
n1 = random.randrange(5)
n2 = int(input('Usuário tente adivinhar que número foi escolhido: '))
if n1 == n2:
    print('PARABÉNS!!! O número está correto!')
else:
    print('Que pena! O número era {} \nTente Denovo!!' .format(n1))