import pandas as pd

json_file = 'hoja_json.json'

data = pd.read_json(json_file)

column_mapping = {
    'Código': 'código',
    'tipo': 'Tipo',
    'año': 'Año',
    'modelo': 'Modelo',
    'marca': 'Marcas',
    'Equivalencia': 'Equivalencia',
    'Fabricante': 'Fabricante',
    'Aplicacion': 'Aplicación'
}

df = data[column_mapping.values()].rename(columns={v: k for k, v in column_mapping.items()})

adicional_columns = [
    'Keyword', 'Oem', 'Titulo', 'Numero dientes', 'Ancho de Polea (mm)'
]

for col in adicional_columns:
    df[col] = None


output_file = 'output.xlsx'
df.to_excel(output_file, index=False)

print(f"El archivo Excel '{output_file}' ha sido creado exitosamente ! ")