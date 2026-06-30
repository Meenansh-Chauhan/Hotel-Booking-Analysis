import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

df = pd.read_csv(
    BASE_DIR / "Data" / "raw" / "Hotel_bookings_final.csv"
)

# Convert dates
df["booking_date"] = pd.to_datetime(df["booking_date"])

# Month extraction
df["booking_month"] = df["booking_date"].dt.month_name()

# -------------------------
# Monthly Bookings
# -------------------------

monthly_bookings = (
    df.groupby("booking_month")
      .size()
      .sort_values(ascending=False)
)

print("\nMONTHLY BOOKINGS")
print(monthly_bookings)

# -------------------------
# Monthly Revenue
# -------------------------

monthly_revenue = (
    df.groupby("booking_month")["selling_price"]
      .sum()
      .sort_values(ascending=False)
)

print("\nMONTHLY REVENUE")
print(monthly_revenue)

# -------------------------
# Length of Stay
# -------------------------

df["check_in_date"] = pd.to_datetime(df["check_in_date"])
df["check_out_date"] = pd.to_datetime(df["check_out_date"])

df["stay_length"] = (
    df["check_out_date"] -
    df["check_in_date"]
).dt.days

print("\nAVERAGE STAY LENGTH")
print(round(df["stay_length"].mean(), 2))

print("\nSTAY LENGTH BY ROOM TYPE")

print(
    df.groupby("room_type")["stay_length"]
      .mean()
      .round(2)
)