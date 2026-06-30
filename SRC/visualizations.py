import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from pathlib import Path

# -----------------------------
# Paths
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "Data" / "raw" / "Hotel_bookings_final.csv"

OUTPUT_DIR = BASE_DIR / "reports" / "figures" / "charts"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# -----------------------------
# Load Data
# -----------------------------

df = pd.read_csv(DATA_PATH)

# -----------------------------
# Styling
# -----------------------------

sns.set_style("whitegrid")

plt.rcParams["figure.figsize"] = (10, 6)
plt.rcParams["font.size"] = 11

print("Dataset Loaded Successfully")

# =====================================================
# Chart 1 : Booking Volume by Channel
# =====================================================

channel_bookings = (
    df["booking_channel"]
    .value_counts()
)

plt.figure()

sns.barplot(
    x=channel_bookings.index,
    y=channel_bookings.values
)

plt.title("Booking Volume by Channel")
plt.xlabel("Booking Channel")
plt.ylabel("Number of Bookings")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "01_booking_volume_by_channel.png",
    dpi=300
)

plt.close()

print("Chart 1 Saved")

# =====================================================
# Chart 2 : Revenue by Channel
# =====================================================

revenue_by_channel = (
    df.groupby("booking_channel")["selling_price"]
      .sum()
      .sort_values(ascending=False)
)

plt.figure()

sns.barplot(
    x=revenue_by_channel.index,
    y=revenue_by_channel.values
)

plt.title("Revenue by Booking Channel")
plt.xlabel("Booking Channel")
plt.ylabel("Revenue (₹)")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "02_revenue_by_channel.png",
    dpi=300
)

plt.close()

print("Chart 2 Saved")

# =====================================================
# Chart 3 : Cancellation Rate by Channel
# =====================================================

cancel_rate = (
    pd.crosstab(
        df["booking_channel"],
        df["booking_status"],
        normalize="index"
    ) * 100
)

cancel_rate = cancel_rate["Cancelled"]

plt.figure()

ax = sns.barplot(
    x=cancel_rate.index,
    y=cancel_rate.values
)

plt.title("Cancellation Rate by Booking Channel")
plt.xlabel("Booking Channel")
plt.ylabel("Cancellation Rate (%)")

# Add labels on top of bars

for i, value in enumerate(cancel_rate.values):
    ax.text(
        i,
        value + 0.3,
        f"{value:.1f}%",
        ha="center"
    )

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "03_cancellation_rate_by_channel.png",
    dpi=300
)

plt.close()

print("Chart 3 Saved")

# =====================================================
# Chart 4 : Cancellation Rate by Room Type
# =====================================================

room_cancel_rate = (
    pd.crosstab(
        df["room_type"],
        df["booking_status"],
        normalize="index"
    ) * 100
)

room_cancel_rate = room_cancel_rate["Cancelled"]

plt.figure()

ax = sns.barplot(
    x=room_cancel_rate.index,
    y=room_cancel_rate.values
)

plt.title("Cancellation Rate by Room Type")
plt.xlabel("Room Type")
plt.ylabel("Cancellation Rate (%)")

# Add labels

for i, value in enumerate(room_cancel_rate.values):
    ax.text(
        i,
        value + 0.3,
        f"{value:.1f}%",
        ha="center"
    )

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "04_cancellation_rate_by_room_type.png",
    dpi=300
)

plt.close()

print("Chart 4 Saved")

# =====================================================
# Chart 5 : Revenue by Star Rating
# =====================================================

star_revenue = (
    df.groupby("star_rating")["selling_price"]
      .sum()
      .sort_index()
)

plt.figure()

ax = sns.barplot(
    x=star_revenue.index,
    y=star_revenue.values
)

plt.title("Revenue by Star Rating")
plt.xlabel("Star Rating")
plt.ylabel("Revenue (₹)")

# Add value labels

for i, value in enumerate(star_revenue.values):
    ax.text(
        i,
        value,
        f"{value/1_000_000:.1f}M",
        ha="center",
        va="bottom"
    )

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "05_revenue_by_star_rating.png",
    dpi=300
)

plt.close()

print("Chart 5 Saved")

# =====================================================
# Chart 6 : Monthly Revenue Trend
# =====================================================

# Convert Date
df["booking_date"] = pd.to_datetime(df["booking_date"])

# Extract Month Number and Month Name

df["month_num"] = df["booking_date"].dt.month

df["month_name"] = df["booking_date"].dt.strftime("%b")

monthly_revenue = (
    df.groupby(["month_num", "month_name"])["selling_price"]
      .sum()
      .reset_index()
      .sort_values("month_num")
)

plt.figure(figsize=(10,6))

ax = sns.lineplot(
    data=monthly_revenue,
    x="month_name",
    y="selling_price",
    marker="o"
)

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue (₹)")

# Add labels

for x, y in zip(
    monthly_revenue["month_name"],
    monthly_revenue["selling_price"]
):
    plt.text(
        x,
        y,
        f"{y/1_000_000:.1f}M",
        ha="center",
        va="bottom"
    )

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "06_monthly_revenue_trend.png",
    dpi=300
)

plt.close()

print("Chart 6 Saved")

# =====================================================
# Chart 7 : Booking Status Distribution
# =====================================================

status_counts = (
    df["booking_status"]
    .value_counts()
)

plt.figure(figsize=(8,8))

plt.pie(
    status_counts.values,
    labels=status_counts.index,
    autopct="%1.1f%%"
)

plt.title("Booking Status Distribution")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "07_booking_status_distribution.png",
    dpi=300
)

plt.close()

print("Chart 7 Saved")

# =====================================================
# Chart 8 : Profit Contribution by Channel
# =====================================================

profit_by_channel = (
    df.groupby("booking_channel")["markup"]
      .sum()
      .sort_values(ascending=False)
)

plt.figure()

ax = sns.barplot(
    x=profit_by_channel.index,
    y=profit_by_channel.values
)

plt.title("Profit Contribution by Channel")
plt.xlabel("Booking Channel")
plt.ylabel("Profit (₹)")

# Add labels

for i, value in enumerate(profit_by_channel.values):
    ax.text(
        i,
        value,
        f"{value/1_000_000:.1f}M",
        ha="center",
        va="bottom"
    )

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "08_profit_contribution_by_channel.png",
    dpi=300
)

plt.close()

print("Chart 8 Saved")