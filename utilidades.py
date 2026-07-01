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