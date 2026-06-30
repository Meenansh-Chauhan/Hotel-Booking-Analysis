import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

df = pd.read_csv(
    BASE_DIR / "Data" / "raw" / "Hotel_bookings_final.csv"
)

# Date Conversion
df["booking_date"] = pd.to_datetime(df["booking_date"])
df["check_in_date"] = pd.to_datetime(df["check_in_date"])

# Lead Time
df["lead_time"] = (
    df["check_in_date"] - df["booking_date"]
).dt.days

print("\nAVERAGE LEAD TIME BY BOOKING STATUS")

print(
    df.groupby("booking_status")["lead_time"]
      .mean()
      .round(2)
)

print("\nLEAD TIME SUMMARY")

print(
    df["lead_time"].describe()
)