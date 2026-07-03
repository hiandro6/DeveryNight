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
    try:
        data = data.split("/")
        data.reverse()
        data = "-".join(data)
        return data
    except:
        print("DATA INVÁLIDA")
        return False