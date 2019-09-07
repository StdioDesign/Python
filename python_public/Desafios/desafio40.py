print("Sistema de Notas do professor!")
n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))

media = (n1 + n2)/2

if media < 5.0:
    print('Média {:.1f} REPROVADO' .format(media))
elif 4.9 < media < 6.9:
    print('Média {:.1f} RECUPERAÇÃO' .format(media))
else:
    print('Média {:.1f} APROVADO'.format(media))