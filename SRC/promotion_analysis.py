import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

df = pd.read_csv(
    BASE_DIR / "Data" / "raw" / "Hotel_bookings_final.csv"
)

print("\nREFUND STATUS")
print(df["refund_status"].value_counts())

print("\nCOUPON USAGE")
print(df["Coupon USed?"].value_counts())

print("\nAVERAGE CASHBACK BY STATUS")

print(
    df.groupby("booking_status")["cashback"]
      .mean()
      .round(2)
)

print("\nAVERAGE COUPON REDEEM BY STATUS")

print(
    df.groupby("booking_status")["coupon_redeem"]
      .mean()
      .round(2)
)

print("\nAVERAGE REFUND AMOUNT BY STATUS")

print(
    df.groupby("booking_status")["refund_amount"]
      .mean()
      .round(2)
)