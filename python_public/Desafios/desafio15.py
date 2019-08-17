d = float(input('Quatos dias alugados? '))
k = float(input('Quantos Km rodados? '))
r = 60*d + k*0.15
print('O total a pagar é de R$ {:.2f}' .format(r))