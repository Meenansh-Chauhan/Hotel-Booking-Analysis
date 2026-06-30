import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

df = pd.read_csv(
    BASE_DIR / "Data" / "raw"  / "Hotel_bookings_final.csv"
)

revenue_by_channel = (
    df.groupby("booking_channel")["selling_price"]
      .sum()
      .sort_values(ascending=False)
)

print("\nRevenue By Channel")
print(revenue_by_channel)

print("\nAverage Booking Value By Channel")

avg_booking = (
    df.groupby("booking_channel")["selling_price"]
      .mean()
      .round(2)
      .sort_values(ascending=False)
)

print(avg_booking)