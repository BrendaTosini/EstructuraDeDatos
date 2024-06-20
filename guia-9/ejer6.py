import re

def urlValida():

    url=input("Ingrese una URL: ")
    pattern=re.compile(r'^(https*|ftp):\/\/(\w+.)+$')
    if pattern.match(url):
        print("Esta URL es válida")
    else:
        print("Esta URL no es válida")

urlValida()