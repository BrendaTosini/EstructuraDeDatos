import csv

instituciones=[] 
with open("organizaciones_dependencia_conjunta.csv", encoding="UTF-8") as org_dep:
    org_dep_read = csv.DictReader(org_dep, delimiter=";")
    for row in org_dep_read:
        if row["institucion_nivel1_descripcion"] == "UNIVERSIDAD DE BUENOS AIRES":
            instituciones.append(row["organizacion_id"])

with open("organizaciones.csv", encoding="UTF-8") as org:
    org_read = csv.DictReader(org, delimiter=";")
    for row in org_read:
        if row["organizacion_id"] in instituciones:
            print(row["institucion_nivel1_descripcion"])