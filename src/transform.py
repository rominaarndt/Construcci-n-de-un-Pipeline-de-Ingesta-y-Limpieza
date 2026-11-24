import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Limpia encabezados, imputa valores nulos y elimina duplicados."""
    df = df.copy()

    # 1. Normalización de encabezados a snake_case
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace(r"[^\w_]", "", regex=True)
    )

    # 2. Manejo justificado de nulos
    num_cols = df.select_dtypes(include=["number"]).columns
    for col in num_cols:
        if df[col].isnull().sum() > 0:
            df[col] = df[col].fillna(df[col].median())

    cat_cols = df.select_dtypes(include=["object", "category"]).columns
    for col in cat_cols:
        if df[col].isnull().sum() > 0:
            if isinstance(df[col].dtype, pd.CategoricalDtype):
                if "Desconocido" not in df[col].cat.categories:
                    df[col] = df[col].cat.add_categories(["Desconocido"])
            df[col] = df[col].fillna("Desconocido")

    # 3. Eliminación de duplicados
    before = len(df)
    df = df.drop_duplicates()
    duplicates_removed = before - len(df)
    print(f"🗑️ Duplicados eliminados: {duplicates_removed}")
    print("🧹 Transformación completada")

    return df