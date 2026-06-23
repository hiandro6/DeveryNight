def formatar_data(data):
  data = data.split("/")
  data.reverse()
  data = "-".join(data)
  return data

def salvar_clientes(ARQUIVO_VENDAS, clientes):
  arquivo = open(ARQUIVO_CLIENTES, "w", encoding="utf-8")
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
  arquivo.close()

ARQUIVO_CLIENTES = "clientes.txt"

clientes = {}


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