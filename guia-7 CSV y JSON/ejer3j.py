import json

org_id=[]
with open("organizaciones_localizacion.json", encoding="utf-8") as archivo:
    dict = json.load(archivo)
    arr_de_dict= dict["data"]
    for diccionario in arr_de_dict:
        if diccionario["partido_id"] == 224:
            org_id.append(diccionario["organizacion_id"])

actividad_economica={}
with open("organizaciones_actividad_economica.json", encoding="utf-8") as archivo:
    dict=json.load(archivo)
    arr_de_dict= dict["data"]
    for diccionario in arr_de_dict:
        if diccionario["organizacion_id"] in org_id:
            ref_valor = actividad_economica.setdefault(diccionario["actividad_economica_id"], 0) 
            ref_valor += 1
            actividad_economica[diccionario["actividad_economica_id"]] = ref_valor

with open("ref_actividad_economica.json", encoding="utf-8") as archivo:
    dict = json.load(archivo)
    arr_de_dict = dict["data"]
    for diccionario in arr_de_dict:
        if diccionario["actividad_economica_id"] in actividad_economica.keys():
            print("{}:{}".format(diccionario["actividad_economica_desc"], actividad_economica[diccionario["actividad_economica_id"]]))          
