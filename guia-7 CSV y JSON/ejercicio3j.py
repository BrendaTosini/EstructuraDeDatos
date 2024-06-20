import json

instituciones=[] 
with open("organizaciones_localizacion.json", encoding="UTF-8") as org_loc:
    org_loc_read = json.load(org_loc)
    for row in org_loc_read["data"]:
        if row["partido_id"] == 224:
            instituciones.append(row["organizacion_id"])

cantidad_de_ins_pro_act={}
with open("organizaciones_actividad_economica.json", encoding="UTF-8") as org_act:
    org_act_read = json.load(org_act)
    for row in org_act_read["data"]:
        if row["organizacion_id"] in instituciones:
            if row["actividad_economica_id"] in cantidad_de_ins_pro_act.keys():
                cantidad_de_ins_pro_act[row["actividad_economica_id"]] += 1
            else:
                cantidad_de_ins_pro_act[row["actividad_economica_id"]] = 1

with open("ref_actividad_economica.json", encoding="UTF-8") as ref_act:
    ref_act_read = json.load(ref_act)
    for row in ref_act_read["data"]:
        if row["actividad_economica_id"] in cantidad_de_ins_pro_act.keys():
            print("{} : {}".format(row["actividad_economica_desc"], cantidad_de_ins_pro_act[row["actividad_economica_id"]]))