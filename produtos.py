from time import sleep

def load_produtos(ARQUIVO_PRODUTOS):
  global produtos
  try:
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
      arquivo.close()


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


def cadastra_produto():
    global post_produto, produtos
    print(post_produto)
    cod_produto = input("INFORME O CÓDIGO DO PRODUTO: ")
    nome = input("INFORME O NOME DO PRODUTO: ")
    preco = float(input("INFORME O PREÇO DO PRODUTO: "))
    categoria = input("INFORME A CATEGORIA DO PRODUTO: ")
    status = True
    sleep(1)
    print("PROCESSANDO...")
    produtos[cod_produto] = [nome, preco, categoria, status]
    sleep(1)
    print("PRODUTO CADASTRADO COM SUCESSO!")


def exibe_produto():
    global produtos, get_produto
    print(get_produto)
    cod_produto = input("INFORME O CÓDIGO DO PRODUTO: ")
    sleep(1)
    print("PROCURANDO PRODUTO...")
    if cod_produto in produtos:
        print("len:", len(produtos[cod_produto])) #apenas para testes
        print(f""" 
        CÓDIGO: {cod_produto}
        NOME: {produtos[cod_produto][0]}
        PREÇO: {produtos[cod_produto][1]}
        CATEGORIA: {produtos[cod_produto][2]}
        """)
    else:
        print("PRODUTO NÃO ENCONTRADO!")



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


