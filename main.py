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


opcao = ""
while opcao != "0":
    sleep(2)
    print(menu_principal)
    opcao = input("DIGITE SUA OPÇÃO: ")
    print("CARREGANDO...")
    sleep(1)

    if opcao == "1":
        print(menu_produtos)
    
    elif opcao == "2":
        print(menu_clientes)

    elif opcao == "3":
        print(menu_vendas)

    elif opcao == "4":
        print(menu_relatorios)
    
    elif opcao == "5":
        print(menu_infos)

    elif opcao == "0":
        print("ENCERRANDO O SISTEMA...")
        sleep(2)
        print("VOLTE SEMPRE!")
        sleep(1)

    else:
        print(menu_invalido)
