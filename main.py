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
  [2] EXIBIR DADOS DO VENDA
  [3] ALTERAR DADOS DO VENDA
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

opcao = ""
while opcao != "0":
    sleep(2)
    print(menu_principal)
    opcao = input("DIGITE SUA OPÇÃO: ")
    print("CARREGANDO...")
    sleep(1)

    if opcao == "1":
        print(menu_produtos)
        opcao2 = input("DIGITE SUA OPÇÃO: ")
        if opcao2 == "1":
            print(post_produto)

        elif opcao2 == "2":
            print(get_produto)

        elif opcao2 == "3":
            print(put_produto)

        elif opcao2 == "4":
            print(del_produto)

        elif opcao == "0":
            print("de volta ao menu principal")

    elif opcao == "2":
        print(menu_clientes)
        opcao2 = input("DIGITE SUA OPÇÃO: ")
        if opcao2 == "1":
            print(post_cliente)
            nome = input("INFORME O NOME DO CLIENTE: ")
            cpf = input("INFORME O CPF DO CLIENTE: ")
            email = input("INFORME O EMAIL DO CLIENTE")
            sleep(1)
            print("PROCESSANDO...")
            sleep(2)
            print("CLIENTE CADASTRADO COM SUCESSO!")
        elif opcao2 == "2":
            print(get_cliente)
            cpf = input("INFORME O CPF DO CLIENTE: ")
            sleep(1)
            print("PROCESSANDO...")
            sleep(2)
            print("""
                  NOME: John Connor
                  CPF: 400.289.220-00
                  EMAIL: exterminadordofuturo@gmail.com""")

        elif opcao2 == "3":
            print(put_cliente)

        elif opcao2 == "4":
            print(del_cliente)

        elif opcao == "0":
            print("de volta ao menu principal")

    elif opcao == "3":
        print(menu_vendas)
        opcao2 = input("DIGITE SUA OPÇÃO: ")
        if opcao2 == "1":
            print(post_venda)

        elif opcao2 == "2":
            print(get_venda)

        elif opcao2 == "3":
            print(put_venda)

        elif opcao2 == "4":
            print(del_venda)

        elif opcao == "0":
            print("de volta ao menu principal")

    elif opcao == "4":
        print(menu_relatorios)
        opcao2 = input("DIGITE SUA OPÇÃO: ")
        print("esse módulo ainda está em desenvolvimento")

    
    elif opcao == "5":
        print(menu_infos)

    elif opcao == "0":
        print("ENCERRANDO O SISTEMA...")
        sleep(2)
        print("VOLTE SEMPRE!")
        sleep(1)

    else:
        print(menu_invalido)
