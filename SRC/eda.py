import pandas as pd
from pathlib import Path

# -------------------------------
# Load Dataset
# -------------------------------

df = pd.read_csv('Data/raw/Hotel_bookings_final.csv')

# -------------------------------
# Convert Dates
# -------------------------------

date_cols = [
    "booking_date",
    "check_in_date",
    "check_out_date",
    "travel_date"
]

for col in date_cols:
    df[col] = pd.to_datetime(df[col], errors="coerce")

print("\nDate Conversion Complete\n")

print(df[date_cols].dtypes)

# -------------------------------
# Basic Statistics
# -------------------------------

print("\nDataset Shape:")
print(df.shape)

print("\nBooking Status Distribution:")
print(df["booking_status"].value_counts())

print("\nBooking Channel Distribution:")
print(df["booking_channel"].value_counts())

print("\nStar Rating Distribution:")
print(df["star_rating"].value_counts())

print("\nRoom Type Distribution:")
print(df["room_type"].value_counts())

# -------------------------------
# possible pattern finding
# -------------------------------

print(df["booking_channel"].unique())
print("\n")
print(df["channel_of_booking"].unique())


print("\nBOOKING STATUS %")
status_pct = (
    df["booking_status"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)
print(status_pct)