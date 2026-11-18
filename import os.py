import pandas as pd
import os
print(os.path.exists("data/processed/salida.parquet"))  # True si existe


print("Buscando archivos .parquet en el proyecto...")
encontrados = []
for raiz, carpetas, archivos in os.walk("."):
    for archivo in archivos:
        if archivo.endswith(".parquet"):
            encontrados.append(os.path.join(raiz, archivo))

if encontrados:
    print("Se encontraron los siguientes archivos:")
    for f in encontrados:
        print(" ->", f)
else:
    print("No hay ningún archivo .parquet generado todavía.")


# 1. Leés el archivo generado
df = pd.read_parquet("data/processed/dataset_procesado.parquet")

# 2. Revisás forma, columnas y tipos de datos
print("Dimensiones (filas, columnas):", df.shape)
print("\nTipos de datos y nulos:")
print(df.info())

# 3. Ves las primeras 5 filas
print("\nPrimeras filas:")
print(df.head())

