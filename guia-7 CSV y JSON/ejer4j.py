import json

org_id=[]
with open("organizaciones_dependencia_conjunta.json", encoding="utf-8") as archivo:
    dict = json.load(archivo)
    arr_de_dict = dict["data"]
    for diccionario in arr_de_dict:
        if diccionario["institucion_nivel1_descripcion"] == "UNIVERSIDAD DE BUENOS AIRES":
            org_id.append(diccionario["organizacion_id"])

with open ("organizaciones.json", encoding="utf-8") as archivo:
    dict = json.load(archivo)
    arr_de_dict= dict["data"]
    for diccionario in arr_de_dict:
        if diccionario["organizacion_id"] in org_id:
            print(diccionario["institucion_nivel1_descripcion"])