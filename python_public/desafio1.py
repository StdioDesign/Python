nome = str(input('Digite seu nome: ')).title().strip()
idade = int(input('Digite sua idade: '))
av1 = float(input('Nota da Avaliação 1: '))
av2 = float(input('Nota da Avaliação 2: '))

media = (av1 + av2)/2

if media >= 6 and idade >= 18:
    print(f'Senhor {nome}, você foi APROVADO para receber a bolsa! PARABÉNS!')
elif media <=6 and idade >= 18:
    print(f'Senhor {nome}, que pena sua media foi {media} você precisava alcançar a média 6')
elif media >=6 and idade <=18:
    print(f'Senhor {nome}, você conseguiu obter a nota solicitada meus parabéns, mas sua idade ainda não é compatível, volte daqui a {18-idade} anos!')
else:
    print(f'Senhor {nome}, você nao conseguiu obter a nota, mas não desanime você ainda é jovem, continue estudando!')