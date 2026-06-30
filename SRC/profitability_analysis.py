import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

df = pd.read_csv(
    BASE_DIR / "Data" / "raw" / "Hotel_bookings_final.csv"
)

profit_by_channel = (
    df.groupby("booking_channel")["markup"]
      .agg(["sum", "mean"])
      .round(2)
)

print("\nPROFITABILITY BY CHANNEL")
print(profit_by_channel)

profit_by_star = (
    df.groupby("star_rating")["markup"]
      .agg(["sum", "mean"])
      .round(2)
)

print("\nPROFITABILITY BY STAR RATING")
print(profit_by_star)

profit_by_room = (
    df.groupby("room_type")["markup"]
      .agg(["sum", "mean"])
      .round(2)
)

print("\nPROFITABILITY BY ROOM TYPE")
print(profit_by_room)