def salvar_vendas(ARQUIVO_VENDAS, vendas):
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
  arquivo_vendas.close()
  

ARQUIVO_VENDAS = "vendas.txt"
vendas = {}

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