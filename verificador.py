def minusculas(password):
    for letra in password:
        if 'a' <= letra <= 'z':  
            return True
    return False

def mayusculas(password):
    for letra in password:
        if 'A' <= letra <= 'Z':  
            return True
    return False

def numeros(password):
    for letra in password:
        if '0' <= letra <= '9':  
            return True
    return False

def mas_de_8_caracteres(password):
    if len(password) > 8:
        return True
    return False
