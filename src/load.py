import os
import pandas as pd


def save_to_parquet(df: pd.DataFrame, output_path: str) -> None:
    """Guarda el DataFrame transformado en formato Parquet."""
    carpeta_destino = os.path.dirname(output_path)
    if carpeta_destino:
        os.makedirs(carpeta_destino, exist_ok=True)

    df.to_parquet(output_path, index=False)
    print(f"✅ Datos exportados exitosamente a: {output_path}")