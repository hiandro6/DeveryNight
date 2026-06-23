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
  

def load_vendas(ARQUIVO_VENDAS):
    global vendas
    try:
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