import csv

org_id = []
with open("organizaciones_localizacion.csv", encoding="UTF-8") as archivo:
    reader = csv.DictReader(archivo, delimiter=";")
    for linea in reader:
        if linea["partido_id"] == "224" and linea["localidad_id"] == "114":
            org_id.append(linea["organizacion_id"])

institucion_id = []
with open("ref_tipo_institucion.csv", encoding="UTF-8") as archivo:
    reader = csv.DictReader(archivo, delimiter=";")
    for linea in reader:
        if linea["tipo_institucion_desc"] == "Empresa":
            institucion_id.append(linea["tipo_institucion_id"])

with open("organizaciones.csv", encoding="UTF-8") as archivo:
    reader = csv.DictReader(archivo, delimiter=";")
    for linea in reader:
        if linea["organizacion_id"] in org_id and linea["tipo_institucion_id"] in institucion_id:
            print(linea["institucion_nivel1_descripcion"])
