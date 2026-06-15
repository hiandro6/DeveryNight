from time import sleep

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

menu_produtos = """
============================
===== MÓDULO PRODUTOS ======
============================

  [1] CADASTRAR PRODUTO
  [2] EXIBIR DADOS DO PRODUTO
  [3] ALTERAR DADOS DO PRODUTO
  [4] EXCLUIR PRODUTO
  [0] RETORNAR AO MENU PRINCIPAL

"""

menu_clientes = """
============================
====== MÓDULO CLIENTES =====
============================

  [1] CADASTRAR CLIENTE
  [2] EXIBIR DADOS DO CLIENTE
  [3] ALTERAR DADOS DO CLIENTE
  [4] EXCLUIR CLIENTE
  [0] RETORNAR AO MENU PRINCIPAL

"""

menu_vendas = """
============================
====== MÓDULO VENDAS =======
============================

  [1] CADASTRAR VENDA
  [2] EXIBIR DADOS DA VENDA
  [3] ALTERAR DADOS DA VENDA
  [4] EXCLUIR VENDA
  [0] RETORNAR AO MENU PRINCIPAL

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



post_produto = """
====================================
=== CADASTRANDO DADOS DO PRODUTO ===
====================================
"""

get_produto = """
====================================
==== EXIBINDO DADOS DO PRODUTO =====
====================================
"""

put_produto = """
====================================
==== ALTERANDO DADOS DO PRODUTO ====
====================================
"""

del_produto = """
====================================
==== DELETANDO DADOS DO PRODUTO ====
====================================
"""





post_cliente = """
====================================
=== CADASTRANDO DADOS DO CLIENTE ===
====================================
"""

get_cliente = """
====================================
==== EXIBINDO DADOS DO CLIENTE =====
====================================
"""

put_cliente = """
====================================
==== ALTERANDO DADOS DO CLIENTE ====
====================================
"""

del_cliente = """
====================================
==== DELETANDO DADOS DO CLIENTE ====
====================================
"""





post_venda = """
====================================
=== CADASTRANDO DADOS DA VENDA =====
====================================
"""

get_venda = """
====================================
===== EXIBINDO DADOS DA VENDA ======
====================================
"""

put_venda = """
====================================
===== ALTERANDO DADOS DA VENDA =====
====================================
"""

del_venda = """
====================================
===== DELETANDO DADOS DA VENDA =====
====================================
"""

produtos = {
    '111' : ["coca 0 lata", 8, "bebidas"],
    '222' : ["pipoca", 5, "lanches"],
    '333' : ["cigarro", 2, "tabacaria"]
}

clientes = {
    '123' : ["Homer Simpson", "homer@springfield.com"],
    '234' : ["Marge Simpson", "marge@springfield.com"],
    '345' : ["Bart Simpson", "bart@springfield.com"],
    '456' : ["Lisa Simpson", "lisa@springfield.com"],
    '678' : ["Maggie Simpson", "maggie@springfield.com"]   
}

vendas = {
    '01' : ["Maico Jackson", [["coca 0 lata", 2], ["pipoca", 3]], 58.50],
    '02' : ["Rick Grimes", [["cigarro", 6], ["isqueiro", 1]], 12.25],
    '03' : ["Luiz Gonzaga", [["cerveja", 3], ["gelo", 1]], 26.98],
}

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
            print(menu_produtos)
            op_produto = input("DIGITE SUA OPÇÃO: ")
            if op_produto == "1":
                print(post_produto)
                cod_produto = int(input("INFORME O CÓDIGO DO PRODUTO: "))
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
                cod_produto = int(input("INFORME O CÓDIGO DO PRODUTO: "))
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
                cod_produto = int(input("INFORME O CÓDIGO DO PRODUTO: "))
                if cod_produto in produtos:
                    nome = input("INFORME O NOME DO PRODUTO: ")
                    preco = float(input("INFORME O PREÇO DO PRODUTO: "))
                    categoria = input("INFORME A CATEGORIA DO PRODUTO: ")
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
        op_cliente = ""
        while op_cliente != "0":
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
        op_venda = ""
        while op_venda != "0":
            print(menu_vendas)
            op_venda = input("DIGITE SUA OPÇÃO: ")
            if op_venda == "1":
                print(post_venda)
                vend_id = int(input("INFORME O ID DA VENDA: "))
                vend_cli = input("INFORME O NOME DO CLIENTE: ")
                comprou_mais = ""
                vend_produtos = []
                while comprou_mais != "N":
                    produto = input("INFORME O NOME DO PRODUTO VENDIDO: ")
                    qnt_produto = int(input(f"INFORME QUANTAS UNIDADES DE {produto} VOCÊ VENDEU PARA {vend_cli}: "))
                    vend_produtos.append([produto, qnt_produto])
                    comprou_mais = input(f"{vend_cli} COMPROU ALGUMA OUTRA COISA NESSA VENDA? [S/N]: ").upper()
                print("PROCESSANDO...")
                sleep(1)
                vend_valor = 500
                vendas[vend_id] = [vend_cli, vend_produtos, vend_valor]
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
                vend_id = int(input("INFORME O ID DA VENDA: "))
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
                    vend_valor = 500
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
        print("ENCERRANDO O SISTEMA...")
        sleep(2)
        print("VOLTE SEMPRE!")
        sleep(1)

    else:
        print(menu_invalido)
