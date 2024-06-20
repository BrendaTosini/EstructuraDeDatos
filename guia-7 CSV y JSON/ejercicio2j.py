import json

empresa_id=0
with open("ref_tipo_institucion.json", encoding="UTF-8") as tipos:
    tipos_read = json.load(tipos)
    for row in tipos_read["data"]:
        if row["tipo_institucion_desc"] == "Empresa":
            empresa_id=row["tipo_institucion_id"]

instituciones=[] 
with open("organizaciones_localizacion.json", encoding="UTF-8") as org_loc:
    org_loc_read = json.load(org_loc)
    for row in org_loc_read["data"]:
        if row["localidad_id"] == 114 and row["partido_id"] == 224:
            instituciones.append(row["organizacion_id"])

with open("organizaciones.json", encoding="UTF-8") as org:
    org_read = json.load(org)
    for row in org_read["data"]:
        if row["organizacion_id"] in instituciones and row["tipo_institucion_id"] == empresa_id:
            print(row["institucion_nivel1_descripcion"])