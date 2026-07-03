from time import sleep
from utilidades import validar_cpf, validar_email, formatar_data, validar_data




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


def load_clientes(ARQUIVO_CLIENTES):
  global clientes
  try:
      arquivo = open(ARQUIVO_CLIENTES,"r",encoding="utf-8")
      for linha in arquivo:
          linha = linha.rstrip()
          campos = linha.split(";")
          clientes[campos[0]] = [campos[1],campos[2], campos[3] == "True", campos[4]]
      arquivo.close()
  except FileNotFoundError:
      clientes = {
      '123': ["Homer Simpson", "homer@springfield.com", True, "1993-10-11"],
      '234': ["Marge Simpson", "marge@springfield.com", True, "1999-12-25"],
      '345': ["Bart Simpson", "bart@springfield.com", True, "2009-06-14"],
      '456': ["Lisa Simpson", "lisa@springfield.com", True, "2011-01-21"],
      '678': ["Maggie Simpson", "maggie@springfield.com", True, "2019-08-01"]
      }
      arquivo = open(ARQUIVO_CLIENTES,"w",encoding="utf-8")
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


def cadastra_cliente():
    global clientes, post_cliente
    print(post_cliente)
    nome = input("INFORME O NOME DO CLIENTE: ")

    while True:
        cpf = input("INFORME O CPF DO CLIENTE: ")
        if validar_cpf(cpf):
            break
        else:
            print("CPF INVÁLIDO")

    while True:
        email = input("INFORME O EMAIL DO CLIENTE: ")
        if validar_email(email):
            break
        else:
            print("EMAIL INVÁLIDO!")

    status = True

    while True:
        nascimento = input("INFORME A DATA DE NASCIMENTO [DD/MM/AAAA]: ")
        if validar_data(nascimento):
            nascimento = formatar_data(nascimento)
            break
        else:
            print("DATA INVÁLIDA!")


    print("PROCESSANDO...")

    clientes[cpf] = [nome, email, status, nascimento]
    sleep(1)
    print("CLIENTE CADASTRADO COM SUCESSO!")
    print("todos os clientes: ", clientes) #apenas para testes


def exibe_cliente():
    global clientes, get_cliente
    print(get_cliente)
    while True:
        cpf = input("INFORME O CPF DO CLIENTE: ")
        if validar_cpf(cpf):
            break
        else:
            print("CPF INVÁLIDO")

    print("PROCURANDO CLIENTE...")
    sleep(1)
    if cpf in clientes:
        print(f"""
        NOME: {clientes[cpf][0]}
        CPF: {cpf}
        EMAIL: {clientes[cpf][1]}
        NASCIMENTO: {clientes[cpf][3]}""")
    else:
        print("CLIENTE NÃO ENCONTRADO! ")


def atualiza_cliente():
    global clientes, put_cliente
    print(put_cliente)

    while True:
        cpf = input("INFORME O CPF DO CLIENTE: ")
        if validar_cpf(cpf):
            break
        else:
            print("CPF INVÁLIDO")

    if cpf in clientes:
        nome = input("INFORME O NOVO NOME DO CLIENTE: ")
        while True:
            email = input("INFORME O EMAIL DO CLIENTE: ")
            if validar_email(email):
                break
            else:
                print("EMAIL INVÁLIDO!")
        status = True

        while True:
            nascimento = input("INFORME A DATA DE NASCIMENTO [DD/MM/AAAA]: ")
            if validar_data(nascimento):
                nascimento = formatar_data(nascimento)
                break
            else:
                print("DATA INVÁLIDA!")

        sleep(1)
        print("PROCESSANDO ALTERAÇÃO...")
        clientes[cpf] = [nome, email, status, nascimento]
        sleep(1)
        print("DADOS DO CLIENTE ALTERADOS COM SUCESSO!")
        print("todos os clientes: ", clientes) #apenas para testes
    else:
        print("CLIENTE NÃO ENCONTRADO")


def deleta_cliente():
    global clientes, del_clientes
    print(del_cliente)
    while True:
        cpf = input("INFORME O CPF DO CLIENTE: ")
        if validar_cpf(cpf):
            break
        else:
            print("CPF INVÁLIDO")
    if cpf in clientes:
        confirma = input("DESEJA MESMO EXCLUIR ESSE CLIENTE? [S/N]: ").upper()
        if confirma == "S":
            sleep(1)
            print("EXCLUINDO CLIENTE...")
            clientes[cpf][2] = False
            sleep(1)
            print("CLIENTE EXCLUIDO COM SUCESSO!")
            print("todos os clientes: ", clientes) #apenas para testes
        else:
            print("EXCLUSÃO CANCELADA!")
    else:
        print("CLIENTE NÃO ENCONTRADO! ")



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