"""
Week 1 - Logistics Data Science
Strategic Planning and Data Exploration

This script provides a starter implementation for the proposed
logistics analytics workflow.

Before execution:
1. Download the DataCo dataset from:
   https://data.mendeley.com/datasets/8gx2fvg2k6/5
2. Verify the exact column names using the dataset description file.
3. Update DATA_PATH and feature names where necessary.
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

DATA_PATH = Path("data/DataCoSupplyChainDataset.csv")


def load_data(path: Path) -> pd.DataFrame:
    """Load the DataCo supply-chain CSV."""
    df = pd.read_csv(path, encoding="latin-1")
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df


def profile_data(df: pd.DataFrame) -> None:
    """Print basic data-quality information."""
    print("Shape:", df.shape)
    print("\nData types:")
    print(df.dtypes)
    print("\nDuplicate rows:", df.duplicated().sum())
    print("\nTop missing-value counts:")
    print(df.isna().sum().sort_values(ascending=False).head(15))


def calculate_late_delivery_rate(df: pd.DataFrame) -> float:
    """
    Calculate late-delivery rate where the dataset contains
    the expected late_delivery_risk field.
    """
    target = "late_delivery_risk"

    if target not in df.columns:
        raise KeyError(
            f"'{target}' not found. Check the official dataset schema."
        )

    return df[target].mean() * 100


def plot_late_rate_by_shipping_mode(df: pd.DataFrame) -> None:
    """Plot late-delivery rate by shipping mode."""
    required = {"shipping_mode", "late_delivery_risk"}

    if not required.issubset(df.columns):
        print("Skipping shipping-mode plot: required columns not found.")
        return

    late_by_mode = (
        df.groupby("shipping_mode")["late_delivery_risk"]
        .mean()
        .mul(100)
        .sort_values(ascending=False)
    )

    late_by_mode.plot(kind="bar")
    plt.title("Late Delivery Rate by Shipping Mode")
    plt.xlabel("Shipping Mode")
    plt.ylabel("Late Delivery Rate (%)")
    plt.tight_layout()
    plt.show()


def main() -> None:
    if not DATA_PATH.exists():
        print("Dataset not found.")
        print("Download it from:")
        print("https://data.mendeley.com/datasets/8gx2fvg2k6/5")
        return

    df = load_data(DATA_PATH)
    profile_data(df)

    try:
        late_rate = calculate_late_delivery_rate(df)
        print(f"\nLate delivery rate: {late_rate:.2f}%")
    except KeyError as exc:
        print(exc)

    plot_late_rate_by_shipping_mode(df)


if __name__ == "__main__":
    main()
