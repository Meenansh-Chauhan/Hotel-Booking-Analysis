import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

df = pd.read_csv(
    BASE_DIR / "Data"/ "raw"  / "Hotel_bookings_final.csv"
)

print("\nUNIQUE CUSTOMERS")

print(df["customer_id"].nunique())

customer_booking_counts = (
    df.groupby("customer_id")
      .size()
)

repeat_customers = (
    customer_booking_counts > 1
).sum()

print("\nREPEAT CUSTOMERS")

print(repeat_customers)

print("\nAVERAGE BOOKINGS PER CUSTOMER")

print(
    round(customer_booking_counts.mean(),2)
)