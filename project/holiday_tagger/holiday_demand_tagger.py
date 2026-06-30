import pandas as pd
import numpy as np
import requests

# ==================================================
# Fetch India Public Holidays - 2024
# ==================================================

YEAR = 2024
COUNTRY_CODE = "IN"

url = (
    f"https://date.nager.at/api/v3/PublicHolidays/"
    f"{YEAR}/{COUNTRY_CODE}"
)

try:

    response = requests.get(
        url,
        timeout=10
    )

    response.raise_for_status()

    holidays = response.json()

    print(
        f"Successfully fetched "
        f"{len(holidays)} holidays."
    )

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
