"""
Week 2 - Logistics Data Collection, Cleaning and Preprocessing

Reference dataset:
DataCo SMART SUPPLY CHAIN FOR BIG DATA ANALYSIS
https://data.mendeley.com/datasets/8gx2fvg2k6/5

Place the downloaded CSV at:
data/raw/DataCoSupplyChainDataset.csv
"""

from pathlib import Path
import pandas as pd
import numpy as np

try:
    from sklearn.preprocessing import StandardScaler, MinMaxScaler
except ImportError:
    StandardScaler = MinMaxScaler = None

RAW_PATH = Path("data/raw/DataCoSupplyChainDataset.csv")
OUTPUT_PATH = Path("data/processed/logistics_cleaned.csv")


def load_data(path: Path) -> pd.DataFrame:
    """Load raw CSV and standardize column names."""
    df = pd.read_csv(path, encoding="latin-1")
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df


def profile_data(df: pd.DataFrame) -> None:
    """Display core data-quality checks."""
    print("Shape:", df.shape)
    print("Duplicate rows:", df.duplicated().sum())

    missing = df.isna().sum().to_frame("missing_count")
    missing["missing_pct"] = missing["missing_count"] / len(df) * 100

    print("\nTop missing-value fields:")
    print(missing.sort_values("missing_pct", ascending=False).head(15))


def clean_exact_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove exact duplicate rows only."""
    return df.drop_duplicates().copy()


def standardize_text(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """Strip whitespace and standardize case for selected text columns."""
    for col in columns:
        if col in df.columns:
            df[col] = (
                df[col]
                .astype("string")
                .str.strip()
                .str.lower()
            )
    return df


def convert_dates(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """Convert date fields and derive useful date features."""
    for col in columns:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")

    order_date = "order_date_(dateorders)"
    if order_date in df.columns:
        df["order_year"] = df[order_date].dt.year
        df["order_month"] = df[order_date].dt.month
        df["order_weekday"] = df[order_date].dt.day_name()

    return df


def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Example missing-value treatment.
    Always validate business meaning before applying these rules.
    """
    if "sales" in df.columns:
        df["sales"] = df["sales"].fillna(df["sales"].median())

    if "shipping_mode" in df.columns:
        df["shipping_mode"] = df["shipping_mode"].fillna("unknown")

    return df


def iqr_outlier_flag(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Create an IQR-based outlier flag without automatically deleting records."""
    if column not in df.columns:
        return df

    series = df[column].dropna()
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1

    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    df[f"{column}_outlier_flag"] = (
        (df[column] < lower) |
        (df[column] > upper)
    ).astype(int)

    return df


def main() -> None:
    if not RAW_PATH.exists():
        print("Raw dataset not found.")
        print(f"Expected location: {RAW_PATH}")
        print("Download from:")
        print("https://data.mendeley.com/datasets/8gx2fvg2k6/5")
        return

    df = load_data(RAW_PATH)

    print("=== BEFORE CLEANING ===")
    profile_data(df)

    # Exact duplicates only; validate dataset grain before broader deduplication.
    df = clean_exact_duplicates(df)

    # Standardize common categorical fields if present.
    df = standardize_text(
        df,
        ["shipping_mode", "customer_segment", "order_region"]
    )

    # Convert dates.
    df = convert_dates(
        df,
        ["order_date_(dateorders)", "shipping_date_(dateorders)"]
    )

    # Handle selected missing values.
    df = handle_missing_values(df)

    # Flag potential sales outliers rather than deleting them automatically.
    df = iqr_outlier_flag(df, "sales")

    print("\n=== AFTER CLEANING ===")
    profile_data(df)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)

    print(f"\nCleaned dataset saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
