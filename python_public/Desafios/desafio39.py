from datetime import date

print("Serviço de alistamento obrigatório!")
ano = int(input("Digite o ano de nascimento: "))

data = date.today()
idade = data.year - ano

if idade < 18:
    print("Calma jovem reconhecemos seu entusiasmo, mas você não pode se alistar agora volte daqui à {} anos " .format(18-idade))
elif idade == 18:
    print("Seja bem vindo ao Alistamento Militar!")
else:
    print("Seu tempo de Alistamento Militar já passou à {} anos, faça-o quanto antes!" .format(idade-18))