from time import sleep
from utilidades import formatar_data, validar_data, validar_cpf
from produtos import produtos
from clientes import clientes



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
            '1': ["Maico Jackson", [["coca zero lata", 2], ["pipoca", 3]], 31, True, "2026-05-05"],
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



def cadastra_venda():
    global vendas, post_venda, produtos, clientes
    print(post_venda)
    vend_id = str(len(vendas) + 1)

    while True:
        cli_cpf = input("INFORME O CPF DO CLIENTE [XXX.XXX.XXX-XX]: ")
        if validar_cpf(cli_cpf):
            if cli_cpf in clientes.keys():
                break
            else:
                print("CPF NÃO CADASTRADO NO NOSSO BANCO DE CLIENTES")
        else:
            print("CPF INVÁLIDO")

    while True:
        vend_data = input("INFORME A DATA DA VENDA [DD/MM/AAAA]:")
        if validar_data(vend_data):
            vend_data = formatar_data(vend_data)
            break
        else:
            print("DATA INVÁLIDA")

    comprou_mais = ""
    vend_produtos = []
    while comprou_mais != "N":
        while True:
            try:
                pro_id = int(input("INFORME O CÓDIGO DO PRODUTO VENDIDO: "))
                if str(pro_id) in produtos.keys():
                    break
                else:
                    print("CÓDIGO NÃO CADASTRADO NO NOSSO BANCO DE PRODUTOS")
            except:
                print("CÓDIGO INVÁLIDO, TENTE DIGITAR UM NÚMERO INTEIRO")
        pro_id = str(pro_id)

        while True:
            try:
                qnt_produto = int(input(f"INFORME QUANTAS UNIDADES DE {produtos[pro_id][0]} VOCÊ VENDEU PARA {clientes[cli_cpf][0]}: "))
                break
            except:
                print("QUANTIDADE INVÁLIDA, TENTE DIGITAR UM NÚMERO INTEIRO")

        vend_produtos.append([produtos[pro_id][0], qnt_produto])
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
    status = True
    vendas[vend_id] = [clientes[cli_cpf][0], vend_produtos, vend_valor, status, vend_data]
    print("VENDA CADASTRADA COM SUCESSO!")
    print("vendas:", vendas)



def exibe_venda():
    global vendas, get_venda
    print(get_venda)
    while True:
        try:
            vend_id = int(input("INFORME O ID DA VENDA: "))
            break
        except:
            print("ID INVÁLIDO, TENTE DIGITAR UM NÚMERO INTEIRO")
    vend_id = str(vend_id)
    print("PROCURANDO VENDA...")
    sleep(1)
    if vend_id in vendas:
        print(f"""
        ID DA VENDA: {vend_id}
        NOME DO CLIENTE: {vendas[vend_id][0]}
        PRODUTOS VENDIDOS: {vendas[vend_id][1]}
        VALOR TOTAL: R$ {vendas[vend_id][2]}
        DATA DA VENDA:  {vendas[vend_id][4]}
        """)
    else:
        print("VENDA NÃO ENCONTRADA!")



def atualiza_venda():
    global vendas, put_venda, produtos, clientes
    print(put_venda)
    while True:
        try:
            vend_id = int(input("INFORME O ID DA VENDA QUE VOCÊ DESEJA ALTERAR: "))
            break
        except:
            print("ID INVÁLIDO, TENTE DIGITAR UM NÚMERO INTEIRO")
    vend_id = str(vend_id)

    if vend_id in vendas:
        while True:
            cli_cpf = input("INFORME O NOVO CPF DO CLIENTE: [XXX.XXX.XXX-XX]")
            if validar_cpf(cli_cpf):
                if cli_cpf in clientes.keys():
                    break
                else:
                    print("CPF NÃO CADASTRADO NO NOSSO BANCO DE CLIENTES")
            else:
                print("CPF INVÁLIDO")

        while True:
            vend_data = input("INFORME A NOVA DATA DA VENDA [DD/MM/AAAA]:")
            if validar_data(vend_data):
                vend_data = formatar_data(vend_data)
                break
            else:
                print("DATA INVÁLIDA")

        comprou_mais = ""
        vend_produtos = []
        while comprou_mais != "N":
            while True:
                try:
                    pro_id = int(input("INFORME O CÓDIGO DO PRODUTO VENDIDO: "))
                    if str(pro_id) in produtos.keys():
                        break
                    else:
                        print("CÓDIGO NÃO CADASTRADO NO NOSSO BANCO DE PRODUTOS")
                except:
                    print("CÓDIGO INVÁLIDO, TENTE DIGITAR UM NÚMERO INTEIRO")
            pro_id = str(pro_id)

            while True:
                try:
                    qnt_produto = int(input(f"INFORME QUANTAS UNIDADES DE {produtos[pro_id][0]} VOCÊ VENDEU PARA {clientes[cli_cpf][0]}: "))
                    break
                except:
                    print("QUANTIDADE INVÁLIDA, TENTE DIGITAR UM NÚMERO INTEIRO")

            vend_produtos.append([produtos[pro_id][0], qnt_produto])
            comprou_mais = input(f"{clientes[cli_cpf][0]} COMPROU ALGUMA OUTRA COISA NESSA VENDA? [S/N]: ").upper()
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

        status = True

        vendas[vend_id] = [clientes[cli_cpf][0], vend_produtos, vend_valor, status, vend_data]

        print("DADOS DA VENDA ALTERADOS COM SUCESSO!")
        print("vendas", vendas) #apenas para testes
    else:
        print("VENDA NÃO ENCONTRADA!")



def deleta_venda():
    global vendas, del_venda
    print(del_venda)
    while True:
        try:
            vend_id = int(input("INFORME O ID DA VENDA QUE VOCÊ DESEJA EXCLUIR: "))
            break
        except:
            print("ID INVÁLIDO, TENTE DIGITAR UM NÚMERO INTEIRO")
    vend_id = str(vend_id)

    if vend_id in vendas:
        confirma = input("DESEJA MESMO EXCLUIR ESSA VENDA? [S/N]: ").upper()
        if confirma == "S":
            print("EXCLUINDO VENDA...")
            sleep(1)
            vendas[vend_id][3] = False
            print("VENDA EXCLUIDA COM SUCESSO!")
        else: 
            print("EXCLUSÃO CANCELADA!")
    else:
        print("VENDA NÃO ENCONTRADA!")





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