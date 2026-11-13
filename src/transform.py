import pandas as pd

def transform_data(df):
  """Limpia, transforma el dataset y escala la columna customer_age."""
  # 1. Eliminar registros duplicados (paso base del pipeline[cite: 7])
  before = len(df)
  df = df.drop_duplicates()
  duplicates_removed = before - len(df)
  print(f"🗑️ Duplicados eliminados: {duplicates_removed}")

  # 2. Escalar la columna customer_age (rango de 18 a 85)
  if "customer_age" in df.columns:
    scaler = StandardScaler()
    # Scikit-learn espera una matriz 2D, por eso usamos doble corchete [[]]
    df["customer_age_scaled"] = scaler.fit_transform(df[["customer_age"]])
    print(
        "📏 Columna customer_age estandarizada correctamente (media 0, desviación"
        " estándar 1)."
    )

  # 3. Optimización básica de memoria para columnas de tipo objeto/texto[cite: 7]
  for column in df.select_dtypes(include=["object"]).columns:
    df[column] = df[column].astype("category")

  print("🧹 Transformación completada")
  return df
    
    
    


   

