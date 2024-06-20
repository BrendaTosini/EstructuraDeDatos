import csv

org_id =[]
with open("organizaciones_localizacion.csv", encoding = "utf-8") as archivo:
    reader= csv.DictReader(archivo, delimiter=";")
    for linea in reader:
        if linea["partido_id"] == "224":
            org_id.append(linea["organizacion_id"])

act_eco_id={}
with open("organizaciones_actividad_economica.csv", encoding="utf-8") as archivo:
    reader= csv.DictReader(archivo, delimiter=";")
    for linea in reader:
        if linea["organizacion_id"] in org_id:
            if linea["actividad_economica_id"] not in act_eco_id:
                act_eco_id[linea["actividad_economica_id"]] = 1
            else:
                act_eco_id[linea["actividad_economica_id"]] += 1

with open("ref_actividad_economica.csv", encoding= "utf-8") as archivo:
    reader = csv.DictReader(archivo, delimiter=";")
    for linea in reader:
        if linea["actividad_economica_id"] in act_eco_id:
            print(f"""{linea["actividad_economica_desc"]} = {act_eco_id[linea["actividad_economica_id"]]}""")




