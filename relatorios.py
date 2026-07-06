from produtos import produtos
from vendas import vendas
from clientes import clientes
from datetime import datetime
from time import sleep
from utilidades import validar_nome, validar_cpf

def lista_produtos():
    for k , v in produtos.items():
        if v[3]:
            print(f"| ID: {k} | NOME: {v[0]} | VALOR: {v[1]}R$ | CATEGORIA: {v[2]}")
            sleep(0.7)

def produtos_da_categoria():
    while True:
        categoria = input("VOCÊ DESEJA VER OS PRODUTOS DE QUAL CATEGORIA? ")
        if validar_nome(categoria):
            break
        else:
            print("CATEGORIA INVÁLIDA! NÃO UTILIZE NÚMEROS OU CARACTERES ESPECIAIS.")
    existe = False
    for k , v in produtos.items():
        if v[3] and v[2] == categoria:
            existe = True
            break

    if existe:
        for k , v in produtos.items():
            if v[3] and v[2] == categoria:
                print(f"| ID: {k} | NOME: {v[0]} | VALOR: {v[1]}R$ | CATEGORIA: {v[2]}")
                sleep(0.7)
    else:
        print("NÃO ENCONTRAMOS NENHUM PRODUTO DESSA CATEGORIA")    

def produtos_valor_especifico():
    while True:
        try:
            val_min = float(input("QUAL O PREÇO MÍNIMO DOS PRODUTOS QUE VOCÊ QUER LISTAR? "))
            val_max = float(input("QUAL O PREÇO MÁXIMO DOS PRODUTOS QUE VOCÊ QUER LISTAR? "))
            if val_min <= val_max and val_min >= 0:
                break
            else:
                print("DIGITE VALORES VÁLIDOS")
        except:
            print("DIGITE VALORES VÁLIDOS")
    existe = False
    for k , v in produtos.items():
        if v[3] and (v[1] >= val_min) and (v[1] <= val_max):
            existe = True
            break
        
    if existe:
        for k , v in produtos.items():
            if v[3] and (v[1] >= val_min) and (v[1] <= val_max):
                print(f"| ID: {k} | NOME: {v[0]} | VALOR: {v[1]}R$ | CATEGORIA: {v[2]}")
                sleep(0.7)
    else:
        print("NÃO TEMOS NENHUM PRODUTO DENTRO DESSA FAIXA DE VALOR") 


def total_produtos_vendidos():
    total_vendas = 0
    total_produtos = 0
    for k, v in vendas.items():
        if v[3]:
            total_vendas += 1
            for produto in v[1]:
                total_produtos += produto[1]
    print(f"o total de produtos vendidos nas {total_vendas} vendas realizadas foi {total_produtos}")




def lista_clientes():
    for k, v in clientes.items():
        if v[2]:
            print(f"| CPF: {k:16} | NOME: {v[0]:25} | EMAIL: {v[1]:25} | NASCIMENTO: {v[3]}")
            sleep(0.7)


def descobre_idade(nascimento):
    nascimento = datetime.strptime(nascimento, "%Y-%m-%d")
    data_atual = datetime.today()
    idade = data_atual.year - nascimento.year
    if (data_atual.month, data_atual.day) < (nascimento.month, nascimento.day):
        idade -= 1

    return idade


def clientes_idade_especifica():
    while True:
        try:
            idade_min = int(input("QUAL A IDADE MÍNIMA DOS CLIENTES QUE VOCÊ DESEJA LISTAR? "))
            idade_max = int(input("QUAL A IDADE MÁXIMA DOS CLIENTES QUE VOCÊ DESEJA LISTAR? "))
            if idade_min <= idade_max and idade_min >= 0:
                break
            else:
                print("DIGITE IDADES VÁLIDAS")
        except:
            print("DIGITE IDADES VÁLIDAS")
    existe = False
    for k, v in clientes.items():
        if v[2] and descobre_idade(v[3]) >= idade_min and descobre_idade(v[3]) <= idade_max:
            existe = True
            print(f"| CPF: {k:16} | NOME: {v[0]:25} | EMAIL: {v[1]:25} | NASCIMENTO: {v[3]}")
            sleep(0.7)
    if not existe:
        print("NÃO ENCONTRAMOS NENHUM CLIENTE COM ESSA IDADE")


def clientes_mes_especifico():
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    meses2 = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    while True:
        mes = input("VOCÊ DESEJA LISTAR OS CLIENTES NASCIDOS EM QUE MÊS? [EX: 06 OU JUNHO]: ").capitalize()
        if mes in meses:
            indice = meses.index(mes)
            mes = meses2[indice]
            break
        elif mes in meses2:
            break
        else:
            print("DIGITE UM MÊS VÁLIDO")

        
    existe = False
    for k, v in clientes.items():
        if v[2]:
            nascimento = v[3].split("-")
            if nascimento[1] == mes:
                existe = True
                print(f"| CPF: {k:16} | NOME: {v[0]:25} | EMAIL: {v[1]:25} | NASCIMENTO: {v[3]}")
                sleep(0.7)
    if not existe:
        print("NÃO ENCONTRAMOS NENHUM CLIENTE NASCIDO NESSE MÊS")


def clientes_prefixo_nome():
    while True:
        prefixo = input("VOCÊ DESEJA LISTAR OS CLIENTES CUJO NOME INICIA COM? ").capitalize()
        if validar_nome(prefixo):
            break
        else:
            print("NOME INVÁLIDO! NÃO UTILIZE NÚMEROS OU CARACTERES ESPECIAIS.")

    existe = False
    for k, v in clientes.items():
        if v[2]:
            quantidade_letras = len(prefixo)
            prefixo_nome = v[0][0:quantidade_letras].capitalize()
            if prefixo_nome == prefixo:
                existe = True
                print(f"| CPF: {k:16} | NOME: {v[0]:25} | EMAIL: {v[1]:25} | NASCIMENTO: {v[3]}")
                sleep(0.7)
    if not existe:
        print(f"NÃO ENCONTRAMOS NENHUM CLIENTE CUJO NOME INICIE COM {prefixo} ")




def lista_vendas():
    for k, v in vendas.items():
        if v[3]:
            print("="*100)
            print(f"ID DA VENDA: {k:4} | NOME DO CLIENTE: {v[0]:25}| VALOR TOTAL: R$ {v[2]:5} | DATA DA VENDA:  {v[4]}")
            print("PRODUTOS VENDIDOS:")
            for i in v[1]:
                print(f" {i[1]}un x {i[0]}")
            sleep(0.7)


def media_valor_vendas():
    valor_total = 0
    quantidade = 0
    for v in vendas.values():
        if v[3]:
            quantidade += 1
            valor_total += v[2]

    media = valor_total / quantidade
    print(f"A MÉDIA DE VALOR DAS {quantidade} VENDAS REALIZADAS É DE {media}R$")


def vendas_mes_especifico():
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    meses2 = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    
    while True:
        mes_desejado = input("VOCÊ DESEJA LISTAR AS VENDAS REALIZADAS EM QUE MÊS? [ EX: DEZEMBRO OU 12]").capitalize()
        if mes_desejado in meses:
            indice = meses.index(mes_desejado)
            mes_desejado = meses2[indice]
            break
        elif mes_desejado in meses2:
            break
        else:
            print("DIGITE UM MÊS VÁLIDO")

    existe = False
    for k, v in vendas.items():
        if v[3]:
            data_venda = v[4].split("-")
            if mes_desejado == data_venda[1]:
                existe = True
                print("="*100)
                print(f"ID DA VENDA: {k:4} | NOME DO CLIENTE: {v[0]:25}| VALOR TOTAL: R$ {v[2]:5} | DATA DA VENDA:  {v[4]}")
                print("PRODUTOS VENDIDOS:")
                for i in v[1]:
                    print(f" {i[1]}un x {i[0]}")
                sleep(0.7)
    if not existe:
        print(f"NÃO ENCONTRAMOS NENHUMA VENDA REALIZADA NESSE MÊS")



def vendas_cliente_especifico():
    while True:
        cliente_cpf = input("INFORME O CPF DO CLIENTE QUE VOCÊ DESEJA LISTAR AS VENDAS REALIZADAS [XXX.XXX.XXX-XX]: ")
        if validar_cpf(cliente_cpf):
            if cliente_cpf in clientes.keys():
                break
            else:
                print("CPF NÃO CADASTRADO NO NOSSO BANCO DE CLIENTES")
        else:
            print("DIGITE UM CPF VÁLIDO")
    existe = False
    for k, v in vendas.items():
        if v[3]:
            if v[0] == clientes[f"{cliente_cpf}"][0]:
                existe = True
                print("="*100)
                print(f"ID DA VENDA: {k:4} | NOME DO CLIENTE: {v[0]:25}| VALOR TOTAL: R$ {v[2]:5} | DATA DA VENDA:  {v[4]}")
                print("PRODUTOS VENDIDOS:")
                for i in v[1]:
                    print(f" {i[1]}un x {i[0]}")
                sleep(0.7)
    if not existe:
        print(f"NÃO ENCONTRAMOS NENHUMA VENDA REALIZADA POR ESSE CLIENTE")


menu_relatorios = """
============================
===== MÓDULO RELATÓRIOS ====
============================

  [1]  LISTA GERAL DE PRODUTOS
  [2]  PRODUTOS DE UMA CATEGORIA ESPECÍFICA
  [3]  PRODUTOS COM VALOR DENTRO DE UM INTERVALO ESPECÍFICO
  [4]  NÚMERO TOTAL DE PRODUTOS VENDIDOS

  [5]  LISTA GERAL DE CLIENTES
  [6]  CLIENTES COM IDADE EM UM INTERVALO ESPECÍFICO
  [7]  CLIENTES NASCIDOS EM UM MÊS ESPECÍFICO
  [8]  CLIENTES CUJO NOME INICIA COM LETRA(S) ESPECÍFICA

  [9]  LISTA GERAL DE VENDAS
  [10] MÉDIA DE VALOR DAS VENDAS REALIZADAS
  [11] VENDAS REALIZADAS EM UM MÊS ESPECÍFICO
  [12] VENDAS REALIZADAS POR UM CLIENTE ESPECÍFICO

  [0] RETORNAR AO MENU PRINCIPAL

"""
