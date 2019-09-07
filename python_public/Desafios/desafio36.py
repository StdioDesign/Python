print('Bem vindo ao Banco ELIF!')
print(('Percebi que você deseja fazer um financiamento de uma casa!'))

valor = float(input('Informe o valor da casa desejada: '))
salario = float(input('Agora informe o seu salário atual: '))
anos = int(input('Gostaria de saber também em quantos anos você gostaria de financiar o imóvel: '))

meses = anos*12
prestacao = valor/meses
tercoSalario = (salario/100)*30

if prestacao <= tercoSalario:
    print('Seu orçamento está pronto! A prestação mensal será de R$ {:.2f}. ' .format(prestacao))
else:
    anosmin = (valor/(tercoSalario*12))
    print('Desculpa o valor não está compatível com sua renda mensal, aconselhamos que tente fazer um orçamento a partir de {:.0f} anos' .format(anosmin))