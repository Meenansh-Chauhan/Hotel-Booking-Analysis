import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

df = pd.read_csv(
    BASE_DIR / "Data" / "raw" / "Hotel_bookings_final.csv"
)

print("\nBOOKINGS BY STAR RATING")

print(
    df["star_rating"]
      .value_counts()
      .sort_index()
)

print("\nREVENUE BY STAR RATING")

print(
    df.groupby("star_rating")["selling_price"]
      .sum()
      .sort_values(ascending=False)
)

print("\nAVERAGE SELLING PRICE BY STAR RATING")

print(
    df.groupby("star_rating")["selling_price"]
      .mean()
      .round(2)
)