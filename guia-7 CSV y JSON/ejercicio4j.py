import json

instituciones=[] 
with open("organizaciones_dependencia_conjunta.json", encoding="UTF-8") as org_dep:
    org_dep_read = json.load(org_dep)
    for row in org_dep_read["data"]:
        if row["institucion_nivel1_descripcion"] == "UNIVERSIDAD DE BUENOS AIRES":
            instituciones.append(row["organizacion_id"])

with open("organizaciones.json", encoding="UTF-8") as org:
    org_read = json.load(org)
    for row in org_read["data"]:
        if row["organizacion_id"] in instituciones:
            print(row["institucion_nivel1_descripcion"])