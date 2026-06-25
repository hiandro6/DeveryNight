from time import sleep
from produtos import produtos, ARQUIVO_PRODUTOS, menu_produtos, get_produto, put_produto, post_produto, del_produto, salvar_produtos, load_produtos, cadastra_produto, exibe_produto, atualiza_produto, deleta_produto
from clientes import clientes, ARQUIVO_CLIENTES, menu_clientes, get_cliente, put_cliente, post_cliente, del_cliente, formatar_data, salvar_clientes, load_clientes, cadastra_cliente, exibe_cliente, atualiza_cliente, deleta_cliente
from vendas import vendas, ARQUIVO_VENDAS, menu_vendas, get_venda, put_venda, post_venda, del_venda, salvar_vendas, load_vendas, cadastra_venda, exibe_venda, atualiza_venda, deleta_venda
from relatorios import menu_relatorios, lista_produtos, produtos_da_categoria, produtos_valor_especifico, total_produtos_vendidos



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


#RECUPERANDO ARQUIVOS TXT:
load_produtos(ARQUIVO_PRODUTOS)
load_clientes(ARQUIVO_CLIENTES)
load_vendas(ARQUIVO_VENDAS)



print("BEM VINDO AO DEVERY NIGHT, SEU SISTEMA DE GESTÃO PARA CONVÊNIENCIA")
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
                print("produtos: ", produtos) #apenas para teste

            elif op_produto == "2":
                exibe_produto()

            elif op_produto == "3":
                atualiza_produto()

            elif op_produto == "4":
                deleta_produto()

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

            elif op_cliente == "2":
                exibe_cliente()

            elif op_cliente == "3":
                atualiza_cliente()

            elif op_cliente == "4":
                deleta_cliente()

            elif op_cliente == "0":
                print("de volta ao menu principal")




#vendas:
    elif op_princ == "3":
        op_venda = ""
        while op_venda != "0":
            print(menu_vendas)
            op_venda = input("DIGITE SUA OPÇÃO: ")

            if op_venda == "1":
                cadastra_venda()

            elif op_venda == "2":
                exibe_venda()

            elif op_venda == "3":
                atualiza_venda()

            elif op_venda == "4":
                deleta_venda()

            elif op_venda == "0":
                print("de volta ao menu principal")




#relatórios:
    elif op_princ == "4":
        while op_relatorio != "0":
            print(menu_relatorios)
            op_relatorio = input("DIGITE SUA OPÇÃO: ")
            if op_relatorio == "1":
                lista_produtos()

            elif op_relatorio == "2":
                produtos_da_categoria()

            elif op_relatorio == "3":
                produtos_valor_especifico()

            elif op_relatorio == "4":
                total_produtos_vendidos()

            elif op_relatorio == "0":
                print("de volta ao menu principal")




#informações:
    elif op_princ == "5":
        print(menu_infos)

    elif op_princ == "0":
        #GRAVANDO NOS ARQUIVOS.TXT
        salvar_produtos(ARQUIVO_PRODUTOS, produtos)
        salvar_clientes(ARQUIVO_CLIENTES, clientes)
        salvar_vendas(ARQUIVO_VENDAS, vendas)

        print("ENCERRANDO O SISTEMA...")
        sleep(1)
        print("VOLTE SEMPRE!")

    else:
        print(menu_invalido)
