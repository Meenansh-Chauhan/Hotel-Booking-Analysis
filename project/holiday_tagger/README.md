# Holiday Proximity Demand Tagger

## Objective

This project integrates public holiday information with hotel booking data to identify whether bookings occurring near public holidays behave differently from regular bookings.

## Data Source

Public holiday data is obtained from the Nager.Date Public Holidays API.

Dataset used:

* Hotel Booking Dataset (12,000 bookings)

## Feature Engineering

Two new features were created:

1. days_from_holiday

   * Minimum number of days between check-in date and nearest public holiday.

2. holiday_adjacent

   * True if check-in date falls within ±2 days of a public holiday.
   * False otherwise.

## Analysis Performed

Compared Holiday Adjacent and Regular bookings across:

* Average Booking Value
* Average Stay Length
* Cancellation Rate

## Key Findings

* Holiday-adjacent bookings represented 8.38% of all bookings.
* Average booking value was similar between groups.
* Holiday bookings stayed slightly longer.
* Holiday bookings exhibited higher cancellation rates.

## Business Recommendation

Consider stricter cancellation policies or shorter free-cancellation windows around holiday periods to reduce revenue leakage caused by elevated cancellation rates.
