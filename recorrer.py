import json

with open('productos.json','r', encoding='utf-8') as file :
    Excel = json.load(file)


productos = []
codigo_anterior = ""
objeto = {}
primer_producto = True

for ex in Excel:

    codigo = ex['_ProductReferenceCodeId (No es posible modificar)']
    clave = ex['FieldName (No es posible modificar)']
    valor = ex['FieldValueName (No es posible modificar)']
    
    # print(codigo_anterior)
    # print(codigo)

    if (ex['FieldId (No es posible modificar)'] == 22):
        continue

    if (codigo != codigo_anterior):
        if(not primer_producto):
            productos.append(objeto)
        else:
            primer_producto = False
        codigo_anterior = codigo
        objeto = {"código": f"{ex['_ProductReferenceCodeId (No es posible modificar)']}", 
        f"{clave}": f"{valor}"}
    else:
        objeto[f"{clave}"] = f"{valor}"

productos.append(objeto)




with open("hoja_json.json", 'w', encoding='utf-8') as file:
    json.dump(productos, file, indent=4, ensure_ascii=False)


    #nuevo = {f"{ex['FieldName (No es posible modificar)']}": f"{ex['FieldValueName (No es posible modificar)']}"}
    # print(producto['_ProductId (No es posible modificar)'])
    #codigo_anterior = ex['_ProductReferenceCodeId (No es posible modificar)']
    