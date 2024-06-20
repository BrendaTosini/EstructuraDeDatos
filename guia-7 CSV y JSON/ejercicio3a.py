import csv

org_id = []
with open("organizaciones_localizacion.csv", encoding="UTF-8") as archivo:
    reader = csv.DictReader(archivo, delimiter=";")
    for linea in reader:
        if linea["partido_id"] == "224":
            org_id.append(linea["organizacion_id"])

actividades = {}
with open("organizaciones_actividad_economica.csv",encoding="UTF-8") as archivo:
    reader = csv.DictReader(archivo, delimiter=";")
    for linea in reader:
        if linea["organizacion_id"] in org_id:
            if linea["actividad_economica_id"] in actividades.keys():
                actividades[linea["actividad_economica_id"]] += 1
            else:
                actividades[linea["actividad_economica_id"]] = 1

with open("ref_actividad_economica.csv", encoding="UTF-8") as archivo:
    reader = csv.DictReader(archivo, delimiter=";")
    for linea in reader:
        if linea["actividad_economica_id"] in actividades.keys():
            print(f"{linea['actividad_economica_desc']} = {actividades[linea['actividad_economica_id']]}")