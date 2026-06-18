from time import sleep
from produtos import produtos, ARQUIVO_PRODUTOS, menu_produtos, get_produto, put_produto, post_produto, del_produto 
from clientes import clientes, ARQUIVO_CLIENTES, menu_clientes, get_cliente, put_cliente, post_cliente, del_cliente 
from vendas import vendas, ARQUIVO_VENDAS, menu_vendas, get_venda, put_venda, post_venda, del_venda



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






try:
    arquivo = open(ARQUIVO_PRODUTOS,"r",encoding="utf-8")
    for linha in arquivo:
        linha = linha.rstrip()
        campos = linha.split(";")
        produtos[campos[0]] = [campos[1],float(campos[2]),campos[3]]
    arquivo.close()
except FileNotFoundError:
    produtos = {
    '111': ["coca 0 lata", 8, "bebidas"],
    '222': ["pipoca", 5, "lanches"],
    '333': ["cigarro", 2, "tabacaria"]
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
            + "\n"
        )
    arquivo.close()



try:
    arquivo = open(ARQUIVO_CLIENTES,"r",encoding="utf-8")
    for linha in arquivo:
        linha = linha.rstrip()
        campos = linha.split(";")
        clientes[campos[0]] = [campos[1],campos[2]]
    arquivo.close()
except FileNotFoundError:
    clientes = {
    '123': ["Homer Simpson", "homer@springfield.com"],
    '234': ["Marge Simpson", "marge@springfield.com"],
    '345': ["Bart Simpson", "bart@springfield.com"],
    '456': ["Lisa Simpson", "lisa@springfield.com"],
    '678': ["Maggie Simpson", "maggie@springfield.com"]
    }
    arquivo = open(ARQUIVO_CLIENTES,"w",encoding="utf-8")
    for cpf in clientes:
        arquivo.write(
            cpf
            + ";"
            + clientes[cpf][0]
            + ";"
            + clientes[cpf][1]
            + "\n"
        )
    arquivo.close()



try:
    arquivo = open(ARQUIVO_VENDAS, "r", encoding="utf-8")
    for linha in arquivo:
        linha = linha.rstrip()
        campos = linha.split(";")

        id_venda = campos[0]
        cliente = campos[1]
        valor = float(campos[3])

        produtos_vendidos = []
        lista_produtos = campos[2].split("|")
        for produto in lista_produtos:
            dados = produto.split(",")
            produtos_vendidos.append([dados[0], int(dados[1])])

        vendas[id_venda] = [cliente, produtos_vendidos, valor]

    arquivo.close()

except FileNotFoundError:

    vendas = {
        '01': ["Maico Jackson", [["coca 0 lata", 2], ["pipoca", 3]], 31],
        '02': ["Rick Grimes", [["cigarro", 1]], 2]
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
            + "\n"
        )

    arquivo.close()






op_princ = ""
while op_princ != "0":
    sleep(1)
    print(menu_principal)
    op_princ = input("DIGITE SUA OPÇÃO: ")
    print("CARREGANDO...")
    sleep(1)




#produtos:
    if op_princ == "1":
        print(menu_produtos)
        op_produto = input("DIGITE SUA OPÇÃO: ")
        if op_produto == "1":
            print(post_produto)
            cod_produto = input("INFORME O CÓDIGO DO PRODUTO: ")
            nome = input("INFORME O NOME DO PRODUTO: ")
            preco = float(input("INFORME O PREÇO DO PRODUTO: "))
            categoria = input("INFORME A CATEGORIA DO PRODUTO: ")
            sleep(1)
            print("PROCESSANDO...")
            produtos[cod_produto] = [nome, preco, categoria]
            sleep(1)
            print("PRODUTO CADASTRADO COM SUCESSO!")
            print("produtos: ", produtos) #apenas para teste

        elif op_produto == "2":
            print(get_produto)
            cod_produto = input("INFORME O CÓDIGO DO PRODUTO: ")
            sleep(1)
            print("PROCURANDO PRODUTO...")
            if cod_produto in produtos:
                print(f""" 
                CÓDIGO: {cod_produto}
                NOME: {produtos[cod_produto][0]}
                PREÇO: {produtos[cod_produto][1]}
                CATEGORIA: {produtos[cod_produto][2]}
                """)
            else:
                print("PRODUTO NÃO ENCONTRADO!")

        elif op_produto == "3":
            print(put_produto)
            cod_produto = input("INFORME O CÓDIGO DO PRODUTO: ")
            if cod_produto in produtos:
                nome = input("INFORME O NOVO NOME DO PRODUTO: ")
                preco = float(input("INFORME O NOVO PREÇO DO PRODUTO: "))
                categoria = input("INFORME A NOVA CATEGORIA DO PRODUTO: ")
                produtos[cod_produto] = [nome, preco, categoria]
                print("PROCESSANDO ALTERAÇÃO...")
                sleep(1)
                print("DADOS DO PRODUTO ALTERADOS COM SUCESSO!")
                print("produtos:", produtos) #apenas para testes
            else:
                print("PRODUTO NÃO ENCONTRADO")

        elif op_produto == "4":
            print(del_produto)
            cod_produto = input("INFORME O CÓDIGO DO PRODUTO: ")
            if cod_produto in produtos:
                confirma = input("DESEJA MESMO EXCLUIR ESSE PRODUTO? [S/N]: ").upper()
                if confirma == "S":
                    print("EXCLUINDO PRODUTO...")
                    del produtos[cod_produto]
                    sleep(1)
                    print("PRODUTO EXCLUIDO COM SUCESSO!")
                    print("produtos:", produtos) #apenas para testes
                else:
                    print("EXCLUSÃO CANCELADA")
            else:
                print("PRODUTO NÃO ENCONTRADO!")

        elif op_produto == "0":
            print("de volta ao menu principal")




#clientes:
    elif op_princ == "2":
        print(menu_clientes)
        op_cliente = input("DIGITE SUA OPÇÃO: ")
        if op_cliente == "1":
            print(post_cliente)
            nome = input("INFORME O NOME DO CLIENTE: ")
            cpf = input("INFORME O CPF DO CLIENTE: ")
            email = input("INFORME O EMAIL DO CLIENTE: ")
            sleep(1)
            print("PROCESSANDO...")
            clientes[cpf] = [nome, email]
            sleep(1)
            print("CLIENTE CADASTRADO COM SUCESSO!")
            print("todos os clientes: ", clientes) #apenas para testes

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
                  EMAIL: {clientes[cpf][1]}""")
            else:
                print("CLIENTE NÃO ENCONTRADO! ")

        elif op_cliente == "3":
            print(put_cliente)
            cpf = input("INFORME O CPF DO CLIENTE: ")
            if cpf in clientes:
                nome = input("INFORME O NOME DO CLIENTE: ")
                email = input("INFORME O EMAIL DO CLIENTE: ")
                sleep(1)
                print("PROCESSANDO ALTERAÇÃO...")
                clientes[cpf] = [nome, email]
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
                    del clientes[cpf]
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
        print(menu_vendas)
        op_venda = input("DIGITE SUA OPÇÃO: ")
        if op_venda == "1":
            print(post_venda)
            vend_id = str(len(vendas) + 1)
            cli_cpf = input("INFORME O CPF DO CLIENTE: ")
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

            vendas[vend_id] = [clientes[cli_cpf][0], vend_produtos, vend_valor]
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
                  """)
            else:
                print("VENDA NÃO ENCONTRADA!")

        elif op_venda == "3":
            print(put_venda)
            vend_id = input("INFORME O ID DA VENDA: ")
            if vend_id in vendas:
                vend_cli = input("INFORME O NOME DO CLIENTE: ")
                comprou_mais = ""
                vend_produtos = []
                while comprou_mais != "N":
                    produto = input("INFORME O NOME DO PRODUTO VENDIDO: ")
                    qnt_produto = int(input(f"INFORME QUANTAS UNIDADES DE {produto} VOCÊ VENDEU PARA {vend_cli}: "))
                    vend_produtos.append([produto, qnt_produto])
                    comprou_mais = input(f"{vend_cli} COMPROU ALGUMA OUTRA COISA NESSA VENDA? [S/N]: ").upper()
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

                vendas[vend_id] = [vend_cli, vend_produtos, vend_valor]

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
                    del vendas[vend_id]
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
        arquivo = open(ARQUIVO_PRODUTOS, "w", encoding="utf-8")

        for cod in produtos:
            arquivo.write(
                cod
                + ";"
                + produtos[cod][0]
                + ";"
                + str(produtos[cod][1])
                + ";"
                + produtos[cod][2]
                + "\n"
            )
        arquivo.close()



        arquivo = open(ARQUIVO_CLIENTES, "w", encoding="utf-8")

        for cpf in clientes:
            arquivo.write(
                cpf
                + ";"
                + clientes[cpf][0]
                + ";"
                + clientes[cpf][1]
                + "\n"
            )
        arquivo.close()



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
                + "\n"
            )
        arquivo.close()

        print("ENCERRANDO O SISTEMA...")
        sleep(1)
        print("VOLTE SEMPRE!")

    else:
        print(menu_invalido)
