n = float(input('Salário do funcionário: '))
if n >= 1250:
    n = ((n/100)*10) + n
else:
    n = ((n/100)*15) + n
print('O novo salário com aumento será: R$ {:.2f}' .format(n))