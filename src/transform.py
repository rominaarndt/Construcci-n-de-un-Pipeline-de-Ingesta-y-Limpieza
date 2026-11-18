import pandas as pd


def normalize_column_names(df):
    """Normaliza los nombres de las columnas del DataFrame."""
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace(r"[^\w_]", "", regex=True)
    )
    return df


def handle_missing_values(df):
    """Elimina registros sin identificador e imputa los valores faltantes."""
    df = df.copy()

    if "id_cliente" in df.columns:
        df = df.dropna(subset=["id_cliente"])

    numeric_columns = df.select_dtypes(include=["number"]).columns
    for column in numeric_columns:
        if df[column].isnull().sum() > 0:
            df[column] = df[column].fillna(df[column].median())

    categorical_columns = df.select_dtypes(include=["object", "category"]).columns
    for column in categorical_columns:
        if df[column].isnull().sum() > 0:
            if isinstance(df[column].dtype, pd.CategoricalDtype):
                df[column] = df[column].cat.add_categories(["Desconocido"])
            df[column] = df[column].fillna("Desconocido")

    return df


def transform_data(df):
    """Limpia y transforma el dataset."""
    before = len(df)
    df = df.drop_duplicates()
    duplicates_removed = before - len(df)
    print(f"🗑️ Duplicados eliminados: {duplicates_removed}")

    df = normalize_column_names(df)
    df = handle_missing_values(df)

    for column in df.select_dtypes(include=["object"]).columns:
        df[column] = df[column].astype("category")

    print("🧹 Transformación completada")
    return df

    
    
    


   

