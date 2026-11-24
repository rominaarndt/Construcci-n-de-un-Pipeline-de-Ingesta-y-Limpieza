import pandas as pd

df = pd.read_parquet("data/processed/dataset_procesado.parquet")

print("Dimensiones (filas, columnas):", df.shape)
print("\nTipos de datos y nulos:")
df.info()

print("\nPrimeras filas:")
print(df.head())
