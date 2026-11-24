import pandas as pd


def extract_data(filepath: str) -> pd.DataFrame:
    """Carga un archivo CSV en un DataFrame aplicando tipos optimizados."""
    dtypes = {
        "transaction_amount": "float32",
        "num_prev_transactions": "int32",
        "transaction_freq_monthly": "int32",
        "distance_from_home_km": "float32",
        "time_since_last_txn_hrs": "float32",
        "is_international": "int8",
        "failed_attempts": "int16",
        "pin_changed_recently": "int8",
        "is_fraud": "int8",
        "fraud_type": "category",
    }

    df = pd.read_csv(filepath, dtype=dtypes)
    print(f"✅ Dataset cargado: {len(df)} filas, {len(df.columns)} columnas")
    return df