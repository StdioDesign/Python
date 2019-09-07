import emoji
import random

print(emoji.emojize('Jokenpô :fist::raised_hand::v:', use_aliases=True))
print('Agente - Prepare-se para perder Senhor Anderson!!!')
print(emoji.emojize(' 1 - :fist:', use_aliases=True))
print(emoji.emojize(' 2 - :raised_hand:', use_aliases=True))
print(emoji.emojize(' 3 - :v:', use_aliases=True))
n = int(input('Agente - Faça sua escolha Senhor Anderson! '))
a = random.randrange(1, 4)
if a == 1:
    print(emoji.emojize(':fist:', use_aliases=True))
elif a == 2:
    print(emoji.emojize(':raised_hand:', use_aliases=True))
elif a == 3:
    print(emoji.emojize(':v:', use_aliases=True))

if n == 1:
    if a == 1:
        print('Agente - Vamos começar novamente Senhor Anderson!')
    elif a == 2:
        print('Agente - Que pena Senhor Anderson você perdeu!')
    elif a == 3:
        print('Agente - Vejo que a sorte está a seu favor, você me enoja Senhor Anderson!')
elif n == 2:
    if a == 2:
        print('Agente - Vamos começar novamente Senhor Anderson!')
    elif a == 3:
        print('Agente - Que pena Senhor Anderson você perdeu!')
    elif a == 1:
        print('Agente - Vejo que a sorte está a seu favor, você me enoja Senhor Anderson!')

elif n == 3:
    if a == 3:
        print('Agente - Vamos começar novamente Senhor Anderson!')
    elif a == 1:
        print('Agente - Que pena Senhor Anderson você perdeu!')
    elif a == 2:
        print('Agente - Vejo que a sorte está a seu favor, você me enoja Senhor Anderson!')
else:
    print('Agente - Você não está me levando a sério Senhor Anderson?')