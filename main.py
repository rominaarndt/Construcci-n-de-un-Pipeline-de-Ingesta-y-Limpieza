from src.extract import extract_data
from src.transform import clean_data
from src.load import save_to_parquet


def main():
    raw_path = "data/raw/dataset.csv"  # Ruta a tu CSV
    output_path = "data/processed/dataset_procesado.parquet"

    df = extract_data(raw_path)
    df_clean = clean_data(df)
    save_to_parquet(df_clean, output_path)

    print("Pipeline ejecutado correctamente.")


if __name__ == "__main__":
    main()