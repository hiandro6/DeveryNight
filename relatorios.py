from produtos import produtos
from vendas import vendas
from clientes import clientes
def lista_produtos():
    for k , v in produtos.items():
        if v[3]:
            print(f"| ID: {k} | NOME: {v[0]} | VALOR: {v[1]}R$ | CATEGORIA: {v[2]}")


def produtos_da_categoria():
    categoria = input("VOCÊ DESEJA VER OS PRODUTOS DE QUAL CATEGORIA?")
    existe = False
    for k , v in produtos.items():
        if v[3] and v[2] == categoria:
            existe = True
            break

    if existe:
        for k , v in produtos.items():
            if v[3] and v[2] == categoria:
                print(f"| ID: {k} | NOME: {v[0]} | VALOR: {v[1]}R$ | CATEGORIA: {v[2]}")
    else:
        print("NÃO TEMOS NENHUM PRODUTO DESSA CATEGORIA")    

def produtos_valor_especifico():
    val_min = float(input("QUAL O PREÇO MÍNIMO DOS PRODUTOS QUE VOCÊ QUER LISTAR?"))
    val_max = float(input("QUAL O PREÇO MÁXIMO DOS PRODUTOS QUE VOCÊ QUER LISTAR?"))
    existe = False
    for k , v in produtos.items():
        if v[3] and (v[1] >= val_min) and (v[1] <= val_max):
            existe = True
            break
        
    if existe:
        for k , v in produtos.items():
            if v[3] and (v[1] >= val_min) and (v[1] <= val_max):
                print(f"| ID: {k} | NOME: {v[0]} | VALOR: {v[1]}R$ | CATEGORIA: {v[2]}")
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
  [8]  CLIENTES CUJO NOME INICIA COM UMA LETRA ESPECÍFICA

  [9]  LISTA GERAL DE VENDAS
  [10] MÉDIA DE VALOR POR VENDA
  [11] VENDAS REALIZADAS EM UM MÊS ESPECÍFICO
  [12] VENDAS REALIZADAS POR UM CLIENTE ESPECÍFICO

  [0] RETORNAR AO MENU PRINCIPAL

"""
