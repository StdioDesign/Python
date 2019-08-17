cidade = input('Digite o nome de sua cidade: ').strip()
primeiroNome = cidade.split()
nome = primeiroNome[0].lower()
print('Sua cidade começa com o nome Santo: {}' .format(nome.find('santo')== 0))