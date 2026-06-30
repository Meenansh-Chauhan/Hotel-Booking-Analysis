import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

df = pd.read_csv(
    BASE_DIR / "Data" / "raw" / "Hotel_bookings_final.csv"
)

print("\nTOP 10 CITIES BY REVENUE")

print(
    df.groupby("city")["selling_price"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

cancel_df = df[df["booking_status"]=="Cancelled"]

print("\nTOP CITIES BY CANCELLATIONS")

print(
    cancel_df["city"]
    .value_counts()
    .head(10)
)