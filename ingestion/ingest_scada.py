import os
import pandas as pd
import kagglehub

OUTPUT_DIR = "data"
OUTPUT_FILE = "scada_data.csv"


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df = df.rename(
        columns={
            "Date/Time": "date_time",
            "LV ActivePower (kW)": "lv_activepower_kw",
            "Wind Speed (m/s)": "wind_speed_ms",
            "Theoretical_Power_Curve (KWh)": "theoretical_power_curve_kwh",
            "Wind Direction (°)": "wind_direction_deg",
        }
    )
    return df


def extract_data() -> pd.DataFrame:
    print("Downloading dataset from Kaggle...")

    dataset_path = kagglehub.dataset_download(
        "berkerisen/wind-turbine-scada-dataset"
    )

    print(f"Dataset downloaded to: {dataset_path}")

    files = os.listdir(dataset_path)
    print("Files found:", files)

    csv_files = [f for f in files if f.endswith(".csv")]
    if not csv_files:
        raise FileNotFoundError("No CSV file found in the downloaded dataset.")

    source_file = os.path.join(dataset_path, csv_files[0])
    print(f"Reading file: {source_file}")

    df = pd.read_csv(source_file)

    print(f"Loaded {len(df)} rows and {len(df.columns)} columns")
    print("Original columns:", list(df.columns))

    df = clean_column_names(df)

    print("Cleaned columns:", list(df.columns))

    return df


def save_to_csv(df: pd.DataFrame) -> str:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    file_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)

    print(f"Saving dataset to {file_path}...")
    df.to_csv(file_path, index=False)

    return file_path


def main() -> None:
    df = extract_data()
    file_path = save_to_csv(df)
    print(f"Done. File saved at: {file_path}")


if __name__ == "__main__":
    main()