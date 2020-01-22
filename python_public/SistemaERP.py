import matplotlib.pyplot as plt
import pymysql.cursors

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='erp',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

autentico = False

def logarCadastrar():
    usuarioExistente = 0
    autenticado = False
    usuarioMaster = False

    if decisao == 1:
        print('#'*20)
        nome = input('Login: ')
        senha = input('Senha: ')
        print('#' * 20)

        for linha in resultado:
            if nome == linha['nome'] and senha == linha['senha']:
                if linha ['nivel'] == 1:
                    usuarioMaster = False
                elif linha ['nivel'] == 2:
                    usuarioMaster = True
                autenticado = True
                break
            else:
                autenticado = False
        if not autenticado:
            print('Login ou senha incorreto')

    elif decisao == 2:
        print('#' * 20)
        print('Faça seu cadastro')
        nome = input('Login: ')
        senha = input('Senha: ')
        print('#' * 20)

        for linha in resultado:
            if nome == linha ['nome']:
                usuarioExistente = 1

        if usuarioExistente == 1:
            print('Login já está em uso')
        elif usuarioExistente == 0:
            try:
                with conexao.cursor() as cursor:
                    cursor.execute('insert into cadastros(nome, senha, nivel) values (%s, %s, %s)', (nome, senha ,1))
                    conexao.commit()
                print('usuario cadastrado com sucesso')
            except:
                print('Erro ao inserir os dados')

    return  autenticado, usuarioMaster

def cadastrarProdutos():
    nome = input('Digite o nome do Produto: ')
    ingredientes = input('Digite os ingredientes dos produtos: ')
    grupo = input('Digite o grupo pertencente a esse produto: ')
    preco = float(input('Digite o preço do produto: '))

    try:
        with conexao.cursor() as cursor:
            cursor.execute('insert into produtos(nome, ingredientes, grupo, preco) values (%s, %s, %s, %s)', (nome, ingredientes,grupo, preco))
            conexao.commit()
            print('Produto Cadastrado!')
    except:
        print('Erro ao inserir os produtos no Bando de Dados')

def listarProdutos():
    produtos = []

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from produtos')
            produtosCadastrados = cursor.fetchall()
    except:
        print('Erro ao Conectar ao Banco de dados')

    for i in produtosCadastrados:
        produtos.append(i)
    if len(produtos) != 0:
        for i in range(0,len(produtos)):
            print(produtos[i])
    else:
        print('Nenhum Produto Cadastrado')

def excluirProdutos():
    idDeletar = int(input('Digite o ID referente ao produto que deseja apagar: '))

    try:
        with conexao.cursor() as cursor:
            cursor.execute(f'delete from produtos where id = {idDeletar}')
    except:
        print('Erro ao excluir o produto')

def listarPedidos():
    pedidos = []
    decision = 0

    while decision != 2:
        pedidos.clear()

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from pedidos')
                listarPedidos = cursor.fetchall()
        except:
            print('Erro ao Conectar com o Banco de Dados')

        for i in listarPedidos:
            pedidos.append(i)
        if len(pedidos) != 0:
            for i in range(0, len(pedidos)):
                print(pedidos[i])
        else:
            print('Nenhum Pedido Feito')

        decision = int(input('[1] PEDIDO ENTREGUE\n'
                             '[2] VOLTAR\n'))
        if decision == 1:
            idDeletar = int(input('Digite o ID do pedido entregue: '))

            try:
                with conexao.cursor() as cursor:
                    cursor.execute(f'delete from pedidos where id = {idDeletar}')
                    print('Produto Entregue')
            except:
                print('Erro ao dar Pedido como Entregue')

def gerarEstatistica():

    nomeProdutos = []
    nomeProdutos.clear()

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from produtos')
            produtos = cursor.fetchall()
    except:
        print('Erro ao fazer consulta no Bando de Dados')

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from estatisticaVendido')
            vendido = cursor.fetchall()
    except:
        print('Erro ao fazer consulta no Bando de Dados')

    estado = int(input('[0] SAIR\n'
                       '[1] PESQUISAR POR NOME\n'
                       '[2] PESQUISAR POR GRUPO\n'))

    if estado == 1:
        decisao3 = int(input('[1] PESQUISAR POR QUANTIDADE DE DINHEIRO\n'
                              '[2] PESQUISAR POR QUANTIDADE UNITÁRIA\n'))

        if decisao3 == 1:
            for i in produtos:
                nomeProdutos.append(i['nome'])

            valores = []
            valores.clear()

            for h in range(0, len(nomeProdutos)):
                somaValor = -1

                for i in vendido:
                    if i['nome'] == nomeProdutos[h]:
                        somaValor += i['preco']
                if somaValor == -1:
                    valores.append(0)

                elif somaValor > 0:
                    valores.append(somaValor + 1)

            plt.plot(nomeProdutos, valores)
            plt.ylabel('Quantidade Vendida em Reais')
            plt.xlabel('Produtos')
            plt.show()

        if decisao3 == 2:
            grupoUnico = []
            grupoUnico.clear()

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('select * from produtos')
                    grupo = cursor.fetchall()
            except:
                print('Erro na Consulta')

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('select * from estatisticaVendido')
                    vendidoGrupo = cursor.fetchall()
            except:
                print('Erro na Consulta')

            for i in grupo:
                grupoUnico.append(i['nome'])
            grupoUnico = sorted(set(grupoUnico))

            qntFinal = []
            qntFinal.clear()

            for h in range(0, len(grupoUnico)):
                qntUnitaria = 0
                for i in vendidoGrupo:
                    if grupoUnico[h] == i['nome']:
                        qntUnitaria += 1
                qntFinal.append(qntUnitaria)

            plt.plot(grupoUnico, qntFinal)
            plt.ylabel('Quantidade unitária vendida')
            plt.xlabel('Produtos')
            plt.show()

    elif estado == 2:
        decisao3 = int(input('[1] PESQUISAR POR QUANTIDADE DE DINHEIRO\n'
                             '[2] PESQUISAR POR QUANTIDADE UNITÁRIA\n'))

        if decisao3 == 1:
            for i in produtos:
                nomeProdutos.append(i['grupo'])

            valores = []
            valores.clear()

            for h in range(0, len(nomeProdutos)):
                somaValor = -1

                for i in vendido:
                    if i['grupo'] == nomeProdutos[h]:
                        somaValor += i['preco']
                if somaValor == -1:
                    valores.append(0)

                elif somaValor > 0:
                    valores.append(somaValor + 1)

            plt.plot(nomeProdutos, valores)
            plt.ylabel('Quantidade Vendida em Reais')
            plt.xlabel('Produtos')
            plt.show()

        if decisao3 == 2:
            grupoUnico = []
            grupoUnico.clear()

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('select * from produtos')
                    grupo = cursor.fetchall()
            except:
                print('Erro na Consulta')

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('select * from estatisticaVendido')
                    vendidoGrupo = cursor.fetchall()
            except:
                print('Erro na Consulta')

            for i in grupo:
                grupoUnico.append(i['grupo'])
            grupoUnico = sorted(set(grupoUnico))

            qntFinal = []
            qntFinal.clear()

            for h in range(0, len(grupoUnico)):
                qntUnitaria = 0
                for i in vendidoGrupo:
                    if grupoUnico[h] == i['grupo']:
                        qntUnitaria += 1
                qntFinal.append(qntUnitaria)

            plt.plot(grupoUnico, qntFinal)
            plt.ylabel('Quantidade unitária vendida')
            plt.xlabel('Produtos')
            plt.show()

while not autentico:
    decisao = int(input('[1] LOGAR\n'
                        '[2] CADASTRAR\n'))

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from cadastros')
            resultado = cursor.fetchall()

    except:
        print('Erro ao conectar no Banco de Dados')

    autentico, usuarioSupremo = logarCadastrar()

if autentico:
    print('Autenticado')

    if usuarioSupremo == True:
        decisaoUsuario = 1

        while decisaoUsuario != 0:
            decisaoUsuario = int(input('[0] SAIR\n'
                                       '[1] CADASTRAR PRODUTOS\n'
                                       '[2] LISTAR PRODUTOS CADASTRADOS\n'
                                       '[3] LISTAR PEDIDOS\n'
                                       '[4] VISUALIZAR ESTATÍSTICA\n'))
            if decisaoUsuario == 1:
                cadastrarProdutos()
            elif decisaoUsuario == 2:
                listarProdutos()

                delete = int(input('[1] EXCLUIR PRODUTO\n'
                                   '[2] VOLTAR\n'))
                if delete == 1:
                    excluirProdutos()

            elif decisaoUsuario == 3:
                listarPedidos()

            elif decisaoUsuario == 4:
                gerarEstatistica()