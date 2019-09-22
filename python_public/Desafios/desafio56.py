media = 0
maisVelho = 0
cont = 0

for c in range(1, 5):
    print('============ PESSOA {} ================'.format(c))
    nome = str(input('Digite um nome: ')).strip()
    idade = int(input('Digite a idade: '))
    sexo = int(input('Digite:\n1 - Maculino\n2 - Feminino\n'))

    media += idade

    if maisVelho < idade and sexo == 1:
        maisVelho = idade
        nomeVelho = nome

    if sexo == 2 and idade < 20:
           cont = cont + 1

    if sexo > 2:
        print('Opção inválida')

print('========================================')

media = media/4

print('A média das idades é {}' .format(media))
print('O homem mais velho é o {} com {} anos' .format(nomeVelho, maisVelho))
if cont != 0:
    print('A quantidade de mulheres que tem menos de 20 anos é igual a {}' .format(cont))
else:
    print('Todas as mulheres tem mais de 20 anos')

#OBS:
#for c in filmes: