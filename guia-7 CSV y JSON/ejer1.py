import csv

org_id =[]
with open ("organizaciones_localizacion.csv", encoding="utf-8") as archivo:
    reader = csv.DictReader(archivo, delimiter=";")
    for linea in reader:
        if linea["localidad_id"] == "114" and linea["partido_id"] == "224":
            org_id.append(linea["organizacion_id"])

with open ("organizaciones.csv", encoding= "utf-8") as archivo:
    reader= csv.DictReader(archivo, delimiter=";")
    for linea in reader:
        if linea["organizacion_id"] in org_id:
            print(linea["institucion_nivel1_descripcion"])