
import pandas as pd
import json

df = pd.read_excel('original.xls')

df.insert(0, 'Index', range(1, len(df) + 1))

json_data = df.to_json(orient='records')

json_object = json.loads(json_data)

output_file = 'productos.json'

with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(json_object, file, indent=4, ensure_ascii=False)


print(f'Archivo JSON generado: {output_file}')


