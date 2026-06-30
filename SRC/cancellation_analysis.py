import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

df = pd.read_csv(
    BASE_DIR / "Data" / "raw" / "Hotel_bookings_final.csv"
)

# Cancellation by Booking Channel

cancel_channel = pd.crosstab(
    df["booking_channel"],
    df["booking_status"],
    normalize="index"
).round(4) * 100

print("\nCancellation Rate By Booking Channel (%)")
print(cancel_channel)

# Cancellation by Star Rating

cancel_star = pd.crosstab(
    df["star_rating"],
    df["booking_status"],
    normalize="index"
).round(4) * 100

print("\nCancellation Rate By Star Rating (%)")
print(cancel_star)

# Cancellation by Room Type

cancel_room = pd.crosstab(
    df["room_type"],
    df["booking_status"],
    normalize="index"
).round(4) * 100

print("\nCancellation Rate By Room Type (%)")
print(cancel_room)