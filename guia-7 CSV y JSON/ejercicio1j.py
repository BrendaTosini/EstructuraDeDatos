import json

instituciones=[] 
with open("organizaciones_localizacion.json", encoding="UTF-8") as org_loc:
    org_loc_read = json.load(org_loc)
    for row in org_loc_read["data"]:
        if row["localidad_id"] == 114 and row["partido_id"] == 224:
            instituciones.append(row["organizacion_id"])

with open("organizaciones.json", encoding="UTF-8") as org:
    org_read = json.load(org)
    for row in org_read["data"]:
        if row["organizacion_id"] in instituciones:
            print(row["institucion_nivel1_descripcion"])