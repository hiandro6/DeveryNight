from time import sleep
from produtos import produtos, ARQUIVO_PRODUTOS, menu_produtos, get_produto, put_produto, post_produto, del_produto, salvar_produtos, load_produtos, cadastra_produto, exibe_produto, atualiza_produto, deleta_produto
from clientes import clientes, ARQUIVO_CLIENTES, menu_clientes, get_cliente, put_cliente, post_cliente, del_cliente, formatar_data, salvar_clientes, load_clientes, cadastra_cliente
from vendas import vendas, ARQUIVO_VENDAS, menu_vendas, get_venda, put_venda, post_venda, del_venda, salvar_vendas, load_vendas



print("BEM VINDO AO DEVERY NIGHT, SEU SISTEMA DE GESTÃO PARA CONVÊNIENCIA")



menu_principal = """
============================
======= DEVERY NIGHT =======
============================

  [1] MÓDULO PRODUTOS
  [2] MÓDULO CLIENTES
  [3] MÓDULO VENDAS
  [4] MÓDULO RELATÓRIOS
  [5] MÓDULO INFORMAÇÕES
  [0] SAIR
  
"""




menu_relatorios = """
============================
===== MÓDULO RELATÓRIOS ====
============================

  [1] LISTA GERAL DE PRODUTOS
  [2] LISTA GERAL DE CLIENTES
  [3] LISTA DE VALORES POR VENDA
  [4] NÚMERO DE PRODUTOS VENDIDOS
  [5] MÉDIA DE VALOR POR VENDA
  [0] RETORNAR AO MENU PRINCIPAL

"""

menu_infos = """
============================
==== MÓDULO INFORMAÇÕES ====
============================

   ############################################
   #  PROJETO DE GESTÃO DE UMA CONVENIÊNCIA   #
   #                                          #
   #  DESENVOLVIDO POR HIANDRO ALEX @hiandro6 #
   #                                          #
   #  LICENÇA PÚBLICA GERAL GNU               #
   #  www.gnu.org/licenses/gpl.html           #
   ############################################

  [0] RETORNAR AO MENU PRINCIPAL

"""

menu_invalido = """
============================
====== OPÇÃO INVÁLIDA ======
============================

   ###############################################
   #                                             #
   # RETORNE AO MENU ANTERIOR E TENTE NOVAMENTE  #
   #                                             #
   ###############################################

  [0]  RETORNAR AO MENU ANTERIOR

"""




#PRODUTOS:
load_produtos(ARQUIVO_PRODUTOS)

"""try:
    arquivo = open(ARQUIVO_PRODUTOS,"r",encoding="utf-8")
    for linha in arquivo:
        linha = linha.rstrip()
        campos = linha.split(";")
        produtos[campos[0]] = [campos[1],float(campos[2]),campos[3], campos[4] == "True"]
    arquivo.close()
except FileNotFoundError:
    produtos = {
    '111': ["coca 0 lata", 8, "bebidas", True],
    '222': ["pipoca", 5, "lanches", True],
    '333': ["cigarro", 2, "tabacaria", True]
    }
    arquivo = open(ARQUIVO_PRODUTOS,"w",encoding="utf-8")
    for cod in produtos:
        arquivo.write(
            cod
            + ";"
            + produtos[cod][0]
            + ";"
            + str(produtos[cod][1])
            + ";"
            + produtos[cod][2]
            + ";"
            + str(produtos[cod][3])
            + "\n"
        )
    arquivo.close()"""


#CLIENTES:

load_clientes(ARQUIVO_CLIENTES)
"""try:
    arquivo = open(ARQUIVO_CLIENTES,"r",encoding="utf-8")
    for linha in arquivo:
        linha = linha.rstrip()
        campos = linha.split(";")
        clientes[campos[0]] = [campos[1],campos[2], campos[3] == "True", campos[4]]
    arquivo.close()
except FileNotFoundError:
    clientes = {
    '123': ["Homer Simpson", "homer@springfield.com", True, "1993-10-11"],
    '234': ["Marge Simpson", "marge@springfield.com", True, "1999-12-25"],
    '345': ["Bart Simpson", "bart@springfield.com", True, "2009-06-14"],
    '456': ["Lisa Simpson", "lisa@springfield.com", True, "2011-01-21"],
    '678': ["Maggie Simpson", "maggie@springfield.com", True, "2019-08-01"]
    }
    arquivo = open(ARQUIVO_CLIENTES,"w",encoding="utf-8")
    for cpf in clientes:
        arquivo.write(
            cpf
            + ";"
            + clientes[cpf][0]
            + ";"
            + clientes[cpf][1]
            + ";"
            + str(clientes[cpf][2])
            + ";"
            + clientes[cpf][3]
            + "\n"
        )
    arquivo.close()"""


#VENDAS:

load_vendas(ARQUIVO_VENDAS)

"""try:
    arquivo = open(ARQUIVO_VENDAS, "r", encoding="utf-8")
    for linha in arquivo:
        linha = linha.rstrip()
        campos = linha.split(";")

        id_venda = campos[0]
        cliente = campos[1]
        valor = float(campos[3])
        status = bool(campos[4])
        data_venda = campos[5]
        produtos_vendidos = []
        lista_produtos = campos[2].split("|")
        for produto in lista_produtos:
            dados = produto.split(",")
            produtos_vendidos.append([dados[0], int(dados[1])])
        vendas[id_venda] = [cliente, produtos_vendidos, valor, status, data_venda]

    arquivo.close()

except FileNotFoundError:

    vendas = {
        '1': ["Maico Jackson", [["coca 0 lata", 2], ["pipoca", 3]], 31, True, "2026-05-05"],
        '2': ["Rick Grimes", [["cigarro", 1]], 2, True, "2026-06-06"]
    }

    arquivo = open(ARQUIVO_VENDAS, "w", encoding="utf-8")

    for id_venda in vendas:

        texto_produtos = ""

        for produto in vendas[id_venda][1]:

            texto_produtos = (
                texto_produtos
                + produto[0]
                + ","
                + str(produto[1])
                + "|"
            )

        texto_produtos = texto_produtos.rstrip("|")

        arquivo.write(
            id_venda
            + ";"
            + vendas[id_venda][0]
            + ";"
            + texto_produtos
            + ";"
            + str(vendas[id_venda][2])
            + ";"
            + str(vendas[id_venda][3])
            + ";"
            + vendas[id_venda][4]
            + "\n"
        )

    arquivo.close()
"""





op_princ = ""
while op_princ != "0":
    sleep(1)
    print(menu_principal)
    op_princ = input("DIGITE SUA OPÇÃO: ")
    print("CARREGANDO...")
    sleep(1)




#produtos:
    if op_princ == "1":
        op_produto = ""
        while op_produto != "0":
            sleep(1)
            print(menu_produtos)
            op_produto = input("DIGITE SUA OPÇÃO: ")
            if op_produto == "1":
                cadastra_produto()
                """print(post_produto)
                cod_produto = input("INFORME O CÓDIGO DO PRODUTO: ")
                nome = input("INFORME O NOME DO PRODUTO: ")
                preco = float(input("INFORME O PREÇO DO PRODUTO: "))
                categoria = input("INFORME A CATEGORIA DO PRODUTO: ")
                status = True
                sleep(1)
                print("PROCESSANDO...")
                produtos[cod_produto] = [nome, preco, categoria, status]
                sleep(1)
                print("PRODUTO CADASTRADO COM SUCESSO!")"""
                print("produtos: ", produtos) #apenas para teste

            elif op_produto == "2":
                exibe_produto()
                """print(get_produto)
                cod_produto = input("INFORME O CÓDIGO DO PRODUTO: ")
                sleep(1)
                print("PROCURANDO PRODUTO...")
                if cod_produto in produtos:
                    print("len:", len(produtos[cod_produto])) #apenas para testes
                    print(f"" 
                    CÓDIGO: {cod_produto}
                    NOME: {produtos[cod_produto][0]}
                    PREÇO: {produtos[cod_produto][1]}
                    CATEGORIA: {produtos[cod_produto][2]}
                    "")
                else:
                    print("PRODUTO NÃO ENCONTRADO!")"""

            elif op_produto == "3":
                atualiza_produto()
                """print(put_produto)
                cod_produto = input("INFORME O CÓDIGO DO PRODUTO: ")
                if cod_produto in produtos:
                    nome = input("INFORME O NOVO NOME DO PRODUTO: ")
                    preco = float(input("INFORME O NOVO PREÇO DO PRODUTO: "))
                    categoria = input("INFORME A NOVA CATEGORIA DO PRODUTO: ")
                    status = True
                    produtos[cod_produto] = [nome, preco, categoria, status]
                    print("PROCESSANDO ALTERAÇÃO...")
                    sleep(1)
                    print("DADOS DO PRODUTO ALTERADOS COM SUCESSO!")
                    print("produtos:", produtos) #apenas para testes
                else:
                    print("PRODUTO NÃO ENCONTRADO")"""

            elif op_produto == "4":
                deleta_produto()
                """print(del_produto)
                cod_produto = input("INFORME O CÓDIGO DO PRODUTO: ")
                if cod_produto in produtos:
                    confirma = input("DESEJA MESMO EXCLUIR ESSE PRODUTO? [S/N]: ").upper()
                    if confirma == "S":
                        print("EXCLUINDO PRODUTO...")
                        print("todos os produtos:", produtos) #testes
                        for i in produtos: #testes
                            print(produtos[i])
                        produtos[cod_produto][3] = False
                        sleep(1)
                        print("PRODUTO EXCLUIDO COM SUCESSO!")
                        print("produtos:", produtos) #apenas para testes
                    else:
                        print("EXCLUSÃO CANCELADA")
                else:
                    print("PRODUTO NÃO ENCONTRADO!")"""

            elif op_produto == "0":
                print("de volta ao menu principal")




#clientes:
    elif op_princ == "2":
        op_cliente = ""
        while op_cliente != "0":
            sleep(1)
            print(menu_clientes)
            op_cliente = input("DIGITE SUA OPÇÃO: ")
            if op_cliente == "1":
                cadastra_cliente()
                """print(post_cliente)
                nome = input("INFORME O NOME DO CLIENTE: ")
                cpf = input("INFORME O CPF DO CLIENTE: ")
                email = input("INFORME O EMAIL DO CLIENTE: ")
                status = True
                nascimento = input("INFORME A DATA DE NASCIMENTO DO CLIENTE [DD/MM/AAAA]:")
                nascimento = formatar_data(nascimento)
                sleep(1)
                print("PROCESSANDO...")

                clientes[cpf] = [nome, email, status, nascimento]
                sleep(1)
                print("CLIENTE CADASTRADO COM SUCESSO!")
                print("todos os clientes: ", clientes) #apenas para testes"""

            elif op_cliente == "2":
                print(get_cliente)
                cpf = input("INFORME O CPF DO CLIENTE: ")
                sleep(1)
                print("PROCURANDO CLIENTE...")
                sleep(1)
                if cpf in clientes:
                    print(f"""
                    NOME: {clientes[cpf][0]}
                    CPF: {cpf}
                    EMAIL: {clientes[cpf][1]}
                    NASCIMENTO: {clientes[cpf][3]}""")
                else:
                    print("CLIENTE NÃO ENCONTRADO! ")

            elif op_cliente == "3":
                print(put_cliente)
                cpf = input("INFORME O CPF DO CLIENTE: ")
                if cpf in clientes:
                    nome = input("INFORME O NOVO NOME DO CLIENTE: ")
                    email = input("INFORME O NOVO EMAIL DO CLIENTE: ")
                    status = True
                    nascimento = input("INFORME A DATA DE NASCIMENTO DO CLIENTE [DD/MM/AAAA]:")
                    nascimento = formatar_data(nascimento)
                    sleep(1)
                    print("PROCESSANDO ALTERAÇÃO...")
                    clientes[cpf] = [nome, email, status, nascimento]
                    sleep(1)
                    print("DADOS DO CLIENTE ALTERADOS COM SUCESSO!")
                    print("todos os clientes: ", clientes) #apenas para testes
                else:
                    print("CLIENTE NÃO ENCONTRADO")

            elif op_cliente == "4":
                print(del_cliente)
                cpf = input("INFORME O CPF DO CLIENTE: ")
                if cpf in clientes:
                    confirma = input("DESEJA MESMO EXCLUIR ESSE CLIENTE? [S/N]: ").upper()
                    if confirma == "S":
                        sleep(1)
                        print("EXCLUINDO CLIENTE...")
                        clientes[cpf][2] = False
                        sleep(1)
                        print("CLIENTE EXCLUIDO COM SUCESSO!")
                        print("todos os clientes: ", clientes) #apenas para testes
                    else:
                        print("EXCLUSÃO CANCELADA!")
                else:
                    print("CLIENTE NÃO ENCONTRADO! ")

            elif op_cliente == "0":
                print("de volta ao menu principal")




#vendas:
    elif op_princ == "3":
        op_venda = ""
        while op_venda != "0":
            print(menu_vendas)
            op_venda = input("DIGITE SUA OPÇÃO: ")
            if op_venda == "1":
                print(post_venda)
                vend_id = str(len(vendas) + 1)
                cli_cpf = input("INFORME O CPF DO CLIENTE: ")
                vend_data = input("INFORME A DATA DA VENDA [DD/MM/AAAA]:")
                vend_data = formatar_data(vend_data)
                comprou_mais = ""
                vend_produtos = []
                while comprou_mais != "N":
                    prod_id = input("INFORME O ID DO PRODUTO VENDIDO: ")
                    qnt_produto = int(input(f"INFORME QUANTAS UNIDADES DE {produtos[prod_id][0]} VOCÊ VENDEU PARA {clientes[cli_cpf][0]}: "))
                    vend_produtos.append([produtos[prod_id][0], qnt_produto])
                    comprou_mais = input(f"{clientes[cli_cpf][0]} COMPROU ALGUMA OUTRA COISA NESSA VENDA? [S/N]: ").upper()
                print("PROCESSANDO...")

                sleep(1)

                vend_valor = 0
                for item_venda in vend_produtos:
                    nome_produto = item_venda[0]
                    quantidade = item_venda[1]
                    for cod in produtos:
                        if produtos[cod][0] == nome_produto:
                            preco = produtos[cod][1]
                            vend_valor = (vend_valor + (preco * quantidade))
                status = True
                vendas[vend_id] = [clientes[cli_cpf][0], vend_produtos, vend_valor, status, vend_data]
                print("VENDA CADASTRADA COM SUCESSO!")
                print("vendas:", vendas)

            elif op_venda == "2":
                print(get_venda)
                vend_id = input("INFORME O ID DA VENDA: ")
                print("PROCURANDO VENDA...")
                sleep(1)
                if vend_id in vendas:
                    print(f"""
                    ID DA VENDA: {vend_id}
                    NOME DO CLIENTE: {vendas[vend_id][0]}
                    PRODUTOS VENDIDOS: {vendas[vend_id][1]}
                    VALOR TOTAL: R$ {vendas[vend_id][2]}
                    DATA DA VENDA:  {vendas[vend_id][4]}
                    """)
                else:
                    print("VENDA NÃO ENCONTRADA!")

            elif op_venda == "3":
                print(put_venda)
                vend_id = input("INFORME O ID DA VENDA QUE VOCÊ DESEJA ALTERAR: ")
                if vend_id in vendas:
                    cli_cpf = input("INFORME O NOVO CPF DO CLIENTE: ")
                    comprou_mais = ""
                    vend_produtos = []
                    vend_data = input("INFORME A NOVA DATA DA VENDA [DD/MM/AAAA]:")
                    vend_data = formatar_data(vend_data)
                    while comprou_mais != "N":
                        prod_id = input("INFORME O ID DO PRODUTO VENDIDO: ")
                        qnt_produto = int(input(f"INFORME QUANTAS UNIDADES DE {produtos[prod_id][0]} VOCÊ VENDEU PARA {clientes[cli_cpf][0]}: "))
                        vend_produtos.append([produtos[prod_id][0], qnt_produto])
                        comprou_mais = input(f"{clientes[cli_cpf][0]} COMPROU ALGUMA OUTRA COISA NESSA VENDA? [S/N]: ").upper()
                    print("PROCESSANDO ALTERAÇÃO...")
                    sleep(1)
                    vend_valor = 0
                    for item_venda in vend_produtos:
                        nome_produto = item_venda[0]
                        quantidade = item_venda[1]
                        for cod in produtos:
                            if produtos[cod][0] == nome_produto:
                                preco = produtos[cod][1]
                                vend_valor = (vend_valor + (preco * quantidade))
                    status = True
                    vendas[vend_id] = [vend_cli, vend_produtos, vend_valor, status, vend_data]

                    print("DADOS DA VENDA ALTERADOS COM SUCESSO!")
                    print("vendas", vendas) #apenas para testes
                else:
                    print("VENDA NÃO ENCONTRADA!")

            elif op_venda == "4":
                print(del_venda)
                vend_id = input("INFORME O ID DA VENDA: ")
                if vend_id in vendas:
                    confirma = input("DESEJA MESMO EXCLUIR ESSA VENDA? [S/N]: ").upper()
                    if confirma == "S":
                        print("EXCLUINDO VENDA...")
                        sleep(1)
                        vendas[vend_id][3] = False
                        print("VENDA EXCLUIDA COM SUCESSO!")
                    else: 
                        print("EXCLUSÃO CANCELADA!")
                else:
                    print("VENDA NÃO ENCONTRADA!")


            elif op_venda == "0":
                print("de volta ao menu principal")




#relatórios:
    elif op_princ == "4":
        print(menu_relatorios)
        opcao2 = input("DIGITE SUA OPÇÃO: ")
        print("esse módulo ainda está em desenvolvimento")




#informações:
    elif op_princ == "5":
        print(menu_infos)

    elif op_princ == "0":

        salvar_produtos(ARQUIVO_PRODUTOS, produtos)
        """arquivo = open(ARQUIVO_PRODUTOS, "w", encoding="utf-8")
        for cod in produtos:
            arquivo.write(
                cod
                + ";"
                + produtos[cod][0]
                + ";"
                + str(produtos[cod][1])
                + ";"
                + str(produtos[cod][2])
                + ";"
                + str(produtos[cod][3])
                + "\n"
            )
        arquivo.close()"""


        salvar_clientes(ARQUIVO_CLIENTES, clientes)
        """arquivo = open(ARQUIVO_CLIENTES, "w", encoding="utf-8")

        for cpf in clientes:
            arquivo.write(
                cpf
                + ";"
                + clientes[cpf][0]
                + ";"
                + clientes[cpf][1]
                + ";"
                + str(clientes[cpf][2])
                + ";"
                + clientes[cpf][3]
                + "\n"
            )
        arquivo.close()"""



        salvar_vendas(ARQUIVO_VENDAS, vendas)
        """
        arquivo_vendas = open(ARQUIVO_VENDAS, "w", encoding="utf-8")
        for id_venda in vendas:
            texto_produtos = ""
            for produto in vendas[id_venda][1]:
                texto_produtos = (
                    texto_produtos
                    + produto[0]
                    + ","
                    + str(produto[1])
                    + "|"
                )

            texto_produtos = texto_produtos.rstrip("|")
            arquivo_vendas.write(
                id_venda
                + ";"
                + vendas[id_venda][0]
                + ";"
                + texto_produtos
                + ";"
                + str(vendas[id_venda][2])
                + ";"
                + str(vendas[id_venda][3])
                + ";"
                + vendas[id_venda][4]
                + "\n"
            )
        arquivo_vendas.close()"""

        print("ENCERRANDO O SISTEMA...")
        sleep(1)
        print("VOLTE SEMPRE!")

    else:
        print(menu_invalido)
