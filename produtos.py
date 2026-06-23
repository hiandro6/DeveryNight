def salvar_produtos(ARQUIVO_PRODUTOS, produtos):
  arquivo = open(ARQUIVO_PRODUTOS, "w", encoding="utf-8")
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
  arquivo.close()


ARQUIVO_PRODUTOS = "produtos.txt"
produtos = {}

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


