import json

codigo_mapeo = {
    "-034": "AC", "-001": "AG", "-092": "BAI", "-056": "BAU", "-057": "VER", "-067": "BUF",
    "-088": "BYC", "-011": "CAS", "-068": "VIN", "-076": "DAM", "-006": "DAY", "-012": "DEL",
    "-055": "DEN", "-062": "DER", "-054": "DIP", "-058": "DNI", "-089": "DOG", "-053": "DOL",
    "-059": "DZE", "-070": "LS", "-091": "EXI", "-036": "FER", "-013": "GAU", "-060": "GEN",
    "-038": "GEN", "-052": "GRI", "-077": "GV", "-037": "HUC", "-063": "IGH", "-061": "IND",
    "-064": "KOB", "-051": "LIF", "-016": "LOC", "-002": "MAG", "-003": "MAN", "-080": "MB",
    "-090": "MIR", "-050": "MLH", "-065": "NAG", "-021": "NAK", "-066": "NAP", "-005": "NGK",
    "-049": "NOS", "-022": "OME", "-009": "ORL", "-071": "ORO", "-048": "OSF", "-018": "OSR",
    "-072": "PAU", "-042": "PER", "-041": "PH", "-039": "PLA", "-095": "PLA", "-024": "RAL",
    "-023": "RAY", "-047": "ROH", "-025": "SOL", "-026": "TAC", "-084": "TEG", "-046": "TEN",
    "-045": "TRI", "-027": "TRI", "-004": "VAL", "-093": "VEY", "-043": "VIC", "-028": "VTH",
    "-040": "VUA", "-044": "WAG", "-029": "WIX", "-030": "ZEN", "-031": "ZM", "-094": "DUR",
    "-032": "COF", "-035": "ETM", "-007": "PAR", "-017": "NEO", "-019": "LUK", "-014": "INA",
    "-015": "FAG", "-020": "MAH", "-010": "VMG", "-075": "WAC", "-073": "KES", "-069": "SAC",
    "-074": "HEL", "-082": "FLO", "-081": "TRW", "-088": "TOT", "-063": "IGH", "-096": "RUL",
    "-097": "TRI", "-099": "IND", "-101": "CLI", "-102": "WAL", "-103": "KLA"
}


with open('productos.json','r', encoding='utf-8') as file :
    Excel = json.load(file)


productos = []
codigo_anterior = ""
objeto = {}
primer_producto = True

for ex in Excel:

    codigo = str(ex['_ProductReferenceCodeId (No es posible modificar)'])
    clave = ex['FieldName (No es posible modificar)']
    valor = ex['FieldValueName (No es posible modificar)']
    


    if (ex['FieldId (No es posible modificar)'] == 22):
        continue


    for sufijo, nuevo_sufijo in codigo_mapeo.items():
        if codigo.endswith(sufijo):
            codigo_modificado = codigo.replace(sufijo, nuevo_sufijo)
            break
    else:
        codigo_modificado = codigo




    if (codigo_modificado != codigo_anterior):
        if(not primer_producto):
            productos.append(objeto)
        else:
            primer_producto = False
        codigo_anterior = codigo_modificado
        objeto = {"código": f"{codigo_modificado}", 
        f"{clave}": f"{valor}"}
    else:
        objeto[f"{clave}"] = f"{valor}"

productos.append(objeto)




with open("hoja_json.json", 'w', encoding='utf-8') as file:
    json.dump(productos, file, indent=4, ensure_ascii=False)


    #nuevo = {f"{ex['FieldName (No es posible modificar)']}": f"{ex['FieldValueName (No es posible modificar)']}"}
    # print(producto['_ProductId (No es posible modificar)'])
    #codigo_anterior = ex['_ProductReferenceCodeId (No es posible modificar)']
    