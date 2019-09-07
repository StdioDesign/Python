print('Olá essa é a calculadora de conversão numérica BOH!')
n = int(input('Digite um número para conversão: '))
conversao = int(input('1 - Binário\n2 - Octal\n3 - Hexadecimal\nDigite o numero correspondente a conversão desejada: '))
if conversao == 1:
    print('Seu valor em Binário será {}' .format(bin(n)))
elif conversao == 2:
    print('Seu valor em Octal será {}'.format(oct(n)))
elif conversao == 3:
    print('Seu valor em Hexadecimal será {}' .format(hex(n)))
else:
    print('Número de converção inválida! Por favor digite o número correspondente as opções acima.')