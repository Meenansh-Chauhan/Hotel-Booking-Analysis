import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

df = pd.read_csv(
    BASE_DIR / "Data" / "raw" / "Hotel_bookings_final.csv"
)

print("\nCANCELLATION RATE BY COUPON USAGE")

print(
    pd.crosstab(
        df["Coupon USed?"],
        df["booking_status"],
        normalize="index"
    ).round(4) * 100
)

print("\nAVERAGE SELLING PRICE BY COUPON USAGE")

print(
    df.groupby("Coupon USed?")["selling_price"]
      .mean()
      .round(2)
)

print("\nAVERAGE MARKUP BY COUPON USAGE")

print(
    df.groupby("Coupon USed?")["markup"]
      .mean()
      .round(2)
)