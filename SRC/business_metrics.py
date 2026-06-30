import pandas as pd
from pathlib import Path

# -------------------------------
# Load Dataset
# -------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

df = pd.read_csv(
    BASE_DIR / "Data" / "raw" / "Hotel_bookings_final.csv"
)

# -------------------------------
# Overall Metrics
# -------------------------------

total_bookings = len(df)

confirmed_bookings = (
    df["booking_status"] == "Confirmed"
).sum()

cancelled_bookings = (
    df["booking_status"] == "Cancelled"
).sum()

failed_bookings = (
    df["booking_status"] == "Failed"
).sum()

# Revenue Metrics

total_revenue = df["selling_price"].sum()

total_cost = df["costprice"].sum()

total_profit = df["markup"].sum()

profit_margin_pct = (
    total_profit / total_revenue
) * 100

# Cancellation Metrics

cancellation_rate = (
    cancelled_bookings / total_bookings
) * 100

failed_rate = (
    failed_bookings / total_bookings
) * 100

# Revenue Lost From Cancelled Bookings

cancelled_revenue = (
    df[df["booking_status"] == "Cancelled"]
    ["selling_price"]
    .sum()
)

cancelled_revenue_pct = (
    cancelled_revenue / total_revenue
) * 100

# Refund Metrics

total_refunds = (
    df["refund_amount"]
    .sum()
)

avg_refund = (
    df["refund_amount"]
    .mean()
)

# -------------------------------
# Print Results
# -------------------------------

print("\n" + "="*60)
print("EXECUTIVE BUSINESS METRICS")
print("="*60)

print(f"\nTotal Bookings: {total_bookings:,}")

print(f"Confirmed Bookings: {confirmed_bookings:,}")
print(f"Cancelled Bookings: {cancelled_bookings:,}")
print(f"Failed Bookings: {failed_bookings:,}")

print(f"\nCancellation Rate: {cancellation_rate:.2f}%")
print(f"Failed Booking Rate: {failed_rate:.2f}%")

print(f"\nTotal Revenue: ₹{total_revenue:,.0f}")
print(f"Total Cost: ₹{total_cost:,.0f}")
print(f"Total Profit (Markup): ₹{total_profit:,.0f}")

print(f"\nProfit Margin: {profit_margin_pct:.2f}%")

print(f"\nRevenue From Cancelled Bookings: ₹{cancelled_revenue:,.0f}")
print(f"Cancelled Revenue Share: {cancelled_revenue_pct:.2f}%")

print(f"\nTotal Refund Amount: ₹{total_refunds:,.2f}")
print(f"Average Refund Amount: ₹{avg_refund:.2f}")

print("\n" + "="*60)