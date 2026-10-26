from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA = PROJECT_ROOT / "data" / "processed" / "kendaraan_2025_sanitized.csv"

def load_sanitized_data(path=DEFAULT_DATA):
    """Load sanitized project data; never requires the raw plate-number field."""
    df = pd.read_csv(path)
    if "plat_nomor" in df.columns:
        raise ValueError("Identifier plat_nomor harus dikeluarkan sebelum analisis/publikasi.")
    return df

def normalize_text_categories(df):
    out = df.copy()
    for col in out.select_dtypes(include=["object", "string"]).columns:
        out[col] = out[col].astype("string").str.strip().replace({"": pd.NA})
    return out
