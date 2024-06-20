import re

def validarPassword():

    password=input("Ingrese la password: ")
    pattern= re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{6,10}')
    if pattern.match(password):
        print("Password Válida")
    else:
        print("Password Inválida")
    


validarPassword()