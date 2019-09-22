from datetime import date
print('Identificação de maior idade.')

data = date.today().year
dmaior = 0
for c in range(0, 7):
    nome = str(input('Digite o nome: '))
    ano = int(input(('Digite o ano de nascimento: ')))
    idade = data - ano
    print('Nome: {} Idade: {}'.format(nome, idade))
    if idade >= 21:
        dmaior = dmaior + 1
dmenor = 7 - dmaior
print('Considerando a maioridade 21 anos, a quantidade de pessoas que já atingiram a fase adulta são {}'.format(dmaior))
print('E a quantidade de pessoas que não atingiram a faze adulta são {}' .format(dmenor))