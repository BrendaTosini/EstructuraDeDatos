import csv 
    
def diccionario_notas(notas,trabajos):
    dict = {}

    with open (notas, encoding="utf-8") as archivo:
        reader = csv.DictReader(archivo, delimiter=";")
        for linea in reader:
            ref_valor = dict.setdefault(linea["legajo"], [0,0,0,0, str])
            """if linea["examen"] == "P1" or linea["examen"] == "R1":
                if int(linea["nota"]) > ref_valor[0]:
                    ref_valor[0]= int(linea["nota"])
            if linea["examen"] == "P2" or linea["examen"] == "R2":
                if int(linea["nota"]) > ref_valor[1]:
                    ref_valor[1]= int(linea["nota"])"""
            posicion = int(linea["examen"][-1])-1
            ref_valor[posicion] = max(int(linea["nota"]),ref_valor[posicion])
            #dict[linea["legajo"]] = ref_valor

    with open(trabajos, encoding="utf-8") as archivo:
        reader = csv.DictReader(archivo, delimiter=";")
        for linea in reader:
            ref_valor = dict.setdefault(linea["legajo"], [0,0,0,0, str])
            if linea["trabajo"] == "tp":
                ref_valor[3] = int(linea["nota"])
                
            elif int(linea["nota"]) >= 4:
                ref_valor[2] +=1

    for legajo, arr_notas in dict.items():
        if arr_notas[0] >= 4 and arr_notas[1] >= 4 and arr_notas[2] >= 2 and arr_notas[3] >= 4:
            arr_notas[4]= "APROBADO"
        elif arr_notas[0] >= 7 and arr_notas[1] >= 7 and arr_notas[2] >= 3 and arr_notas[3] >= 4:
            arr_notas[4]= "PROMOCIONA"  
        else:
            arr_notas[4]= "REPROBADO"
        #dict[legajo] = (arr_notas[0], arr_notas[1], arr_notas[2],arr_notas[3],arr_notas[4])
        arr_notas= tuple(arr_notas)
        dict[legajo] = arr_notas


    return dict       


dict = diccionario_notas("notas.csv","trabajos.csv")
print(dict)

 