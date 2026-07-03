from datetime import datetime


def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "").strip()
    if not cpf.isdigit():
        return False
        
    if len(cpf) != 11:
        return False

    return True


def validar_email(email):
    email = email.strip()
    if "@" not in email:
        return False

    if "." not in email:
        return False

    if email.count("@") != 1:
        return False

    return True



def validar_data(data):
    try:
        data = datetime.strptime(data, "%d/%m/%Y")

        if data > datetime.now():
            return False

        return True
    except ValueError:
        return False

def formatar_data(data):
    data = data.split("/")
    data.reverse()
    data = "-".join(data)
    return data


def validar_nome(nome):
    nome = nome.strip()
    if nome == "":
        return False

    for caractere in nome:
        if not (caractere.isalpha() or caractere.isspace()):
            return False

    return True


def menu_invalido():
    print("""
============================
====== OPÇÃO INVÁLIDA ======
============================

   ###############################################
   #                                             #
   # RETORNE AO MENU ANTERIOR E TENTE NOVAMENTE  #
   #                                             #
   ###############################################

""")
    input("PRESSIONE ENTER PARA CONTINUAR... ")


def menu_infos():
    print("""
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

""")
    input("PRESSIONE ENTER PARA RETORNAR AO MENU ANTERIOR... ")