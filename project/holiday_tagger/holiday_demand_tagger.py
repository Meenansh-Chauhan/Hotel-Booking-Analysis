import pandas as pd
import numpy as np
import requests

# ==================================================
# Fetch India Public Holidays - 2024
# ==================================================

YEAR = 2024
COUNTRY_CODE = "IN"

url = (
    f"https://date.nager.at/api/v3/PublicHolidays/."
    f"{YEAR}/{COUNTRY_CODE}"
)

try:
    response = requests.get(
        url,
        timeout=10,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )

    print("Status Code:", response.status_code)
    print("Content-Type:", response.headers.get("Content-Type"))
    print("\nResponse Preview:\n")
    print(response.text[:500])      # Print first 500 characters

    response.raise_for_status()

    holidays = response.json()

    print(f"Successfully fetched {len(holidays)} holidays.")
        
        # Convert API response to DataFrame
    holiday_df = pd.DataFrame(holidays)

    # Keep only useful columns
    holiday_df = holiday_df[
        [
            "date",
            "localName",
            "name",
            "countryCode",
            "fixed",
            "global",
            "types"
        ]
    ]

    # Convert date column to datetime
    holiday_df["date"] = pd.to_datetime(holiday_df["date"])

    # Save as CSVs
    holiday_df.to_csv(
        "../data/processed/holiday_calendar.csv",
        index=False
    )

    print("holiday_calendar.csv saved successfully.")

except requests.exceptions.RequestException as e:

    print(
        f"API Request Failed: {e}"
    )

    holidays = []

holiday_dates = pd.to_datetime(
    [
        holiday["date"]
        for holiday in holidays
    ]
)

holiday_dates
