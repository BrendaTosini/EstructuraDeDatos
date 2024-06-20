import csv

org_id =[]
with open ("organizaciones_localizacion.csv", encoding="utf-8") as archivo:
    reader = csv.DictReader(archivo, delimiter=";")
    for linea in reader:
        if linea["localidad_id"] == "114" and linea["partido_id"] == "224":
            org_id.append(linea["organizacion_id"])

empresas_id =[]
with open ("ref_tipo_institucion.csv", encoding="utf-8") as archivo:
    reader= csv.DictReader(archivo, delimiter=";")
    for linea in reader:
        if linea["tipo_institucion_desc"] == "Empresa":
            empresas_id.append(linea["tipo_institucion_id"])
    
            

with open ("organizaciones.csv", encoding= "utf-8") as archivo:
    reader= csv.DictReader(archivo, delimiter=";")
    for linea in reader:
        if linea["tipo_institucion_id"] in empresas_id:
            print(linea["institucion_nivel1_descripcion"])