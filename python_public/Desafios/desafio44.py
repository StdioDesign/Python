print('Simulação de pagamento ELIF')
produto = float(input('Digite o valor do produto: '))
print('Formas de Pagamento:')
print('1 - Dinheiro')
print('2 - Cheque')
print('3 - Débito')
print('4 - Cartão de Credito')
p = int(input('Digite o Número correspondente a forma de pagamento: '))

if p == 1 or p == 2:
    produto = produto - (produto/100)*10
    print('Seu pagamento será de R$ {:.2f}' .format(produto))
elif p == 3:
    produto = produto - (produto / 100) * 5
    print('Seu pagamento será de R$ {:.2f}'.format(produto))
elif p == 4:
    parcela = int(input('Digite o numero de parcelas: '))
    if parcela <= 2:
        print('Seu pagamento será de R$ {:.2f}'.format(produto))
    else:
        produto = produto + (produto / 100) * 20
        mensalidade = produto / parcela
        print('Seu pagamento será em {}x de R$ {:.2f}'.format(parcela, mensalidade))
else:
    print('Opção Inválida')