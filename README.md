# Hotel Booking Analytics — Combined Project

## Project Overview

This project presents a full-stack data analytics study of hotel booking behavior across two complementary datasets comprising 42,000 booking transactions from an online travel platform. The analysis spans the complete analytics lifecycle: raw data ingestion, SQL schema design, Python-based exploratory analysis, discount and loyalty decomposition, holiday demand engineering, and executive dashboard delivery.

The work integrates two independent analyses — one focused on channel performance, cancellation root cause analysis, and business profitability (30,000 records), and a second focused on discount strategy, OTA behavior, coupon effectiveness, and data engineering (12,000 records) — into a single coherent business narrative.

## Portfolio Highlights

✓ 42,000 Booking Records

✓ 4 Relational SQL Tables

✓ 35+ DAX Measures

✓ 3 Interactive Power BI Pages

✓ 20+ Business KPIs

✓ Python ETL Pipeline

✓ SQL Window Functions

✓ Executive Dashboard

✓ Business Recommendations

## Business Objectives


Which booking channels deliver the highest revenue, profit, and booking quality — and why?
What are the structural causes of the platform's 20%+ cancellation rate, and where is revenue leakage concentrated?
Are discount and coupon programs improving customer retention or eroding margin?
How does holiday proximity affect booking behavior and cancellation risk?
What customer segments and loyalty tiers represent the largest untapped retention opportunity?
What is the recommended strategic roadmap for improving platform profitability?



## Dataset Overview

Dataset ADataset BRecords30,00012,000Features2420+CoverageChannel, room type, star rating, cancellation, profitability, seasonalityDiscount intensity, OTA behavior, coupon effectiveness, loyalty tiers, holiday demand, SQL schemaTime PeriodMulti-year (booking_date driven)Oct 2021 – Dec 2024


### Key Variables (Shared Across Datasets)

booking_channel — Web / OTA / Travel Agent / Corporate Portal / Direct Website
booking_status — Confirmed / Completed / Cancelled / Failed / No-Show
room_type — Standard / Deluxe / Suite
star_rating — 3 / 4 / 5 star
selling_price / total_amount — Gross booking value
markup / discount_amount — Profitability and discount tracking
coupon_code / coupon_used — Promotional usage flag
customer_loyalty_tier — None / Silver / Gold / Platinum
customer_segment — Individual / Corporate / Group
checkin_date / checkout_date — Stay duration derivation



## Methodology

The analysis followed a structured business analytics workflow across both datasets:


Data Quality Audit — null detection, invalid stays, zero-room bookings, pre-signup records
Schema Design — normalized 4-table relational model (Customers, Properties, Bookings, Reviews)
Exploratory Data Analysis — distribution profiling, outlier detection, type standardization
Channel Performance Analysis — volume, revenue, profit, and cancellation by channel
Discount Decomposition — discount intensity by channel, OTA customer composition analysis
Coupon Effectiveness Analysis — cancellation rate, per-room value, and repeat behavior by coupon usage
Cancellation Root Cause Analysis — channel, room type, lead time, and holiday proximity
Loyalty & Segment Analysis — tier distribution, segment mix, OTA vs platform comparison
Seasonality & Revenue Trend Analysis — monthly revenue, cumulative growth, stay length
Holiday Demand Engineering — API-driven holiday tagger, ±2 day adjacency feature
SQL Analysis — window functions (DENSE_RANK, cumulative SUM OVER) on completed bookings
Business Recommendation Development — prioritized strategic roadmap



## Key Business Metrics

Dataset A — Platform Overview (30,000 Bookings)

MetricValueTotal Bookings30,000Confirmed Bookings21,672Cancelled Bookings6,070Failed Bookings2,258Cancellation Rate20.23%Total Revenue₹885.14 MillionTotal Profit (Markup)₹208.90 MillionProfit Margin23.60%Revenue at Risk (Cancellations)₹179.66 MillionTotal Refunds Issued₹9.63 Million

Dataset B — Discount & Loyalty Platform (12,000 Bookings)

MetricValueTotal Bookings12,000Unique Customers800Unique Properties60Completed Bookings9,333 (77.78%)Cancelled Bookings2,302 (19.18%)No-Show Bookings365 (3.04%)Realized Revenue₹294.86 MillionBooked Revenue (Gross)₹375.76 MillionPlatform Discount Intensity5.33%OTA Discount Intensity7.30% (+1.97pp vs platform)Recoverable Margin (OTA Coupon Optimization)₹4.86 Million


## Key Findings Summary

1. Channel Performance


The Web / Direct Website channel is the strongest performer across all datasets: highest booking volume, revenue, profit, and lowest cancellation rate (17.64%).
OTA drives significant volume but at the highest discount intensity (7.30%) — 1.97 percentage points above the platform average of 5.33%.
Travel Agent bookings have the highest cancellation rate (27.93%) and the weakest overall efficiency.
Corporate Portal is the most margin-efficient intermediary channel, with a discount intensity of only 4.14%.


2. Discount & Coupon Strategy


Platform-wide discount intensity is 5.33%, but OTA alone drives this up by nearly 2 percentage points.
OTA's elevated discounts are not explained by loyalty mix or city mix — OTA simply attracts more Individual travelers (+7.72pp vs platform average), who are more price-sensitive.
Coupon users generate 13.45% lower per-room value than non-coupon users.
Coupon usage reduces cancellation rate by only 0.61 percentage points — a marginal impact that does not justify the revenue cost.
Coupon users show 2.11pp lower repeat booking rate, indicating promotions attract transactional rather than loyal customers.
Reducing OTA coupon spend by 50% is estimated to recover ₹4.86 Million in margin with manageable cancellation risk.


3. Cancellation Analysis


Overall cancellation rate: 20.23% (Dataset A) / 19.18% (Dataset B).
Travel Agent channel: 27.93% — highest among all channels.
Standard rooms: 23.30% — highest among room types, driven by price sensitivity.
Deluxe rooms: 16.02% — best booking quality.
Holiday-adjacent bookings: 22.17% cancellation rate vs 18.91% for regular bookings.
Booking lead time does not predict cancellation — cancelled, confirmed, and failed bookings all share nearly identical lead times (~30 days), ruling out lead time as a lever.


4. Room Type & Property Performance


Standard rooms account for 49.49% of all bookings and generate the highest total profit by volume, but also the highest cancellation rate.
Deluxe rooms (35.74% of bookings) demonstrate the strongest booking quality.
Mid-Range properties represent the largest property segment (39.57%), followed by Budget (31.43%), Premium (17.38%), and Luxury (11.61%).
Standard rooms are the most booked room type across all property categories (confirmed via SQL DENSE_RANK analysis).


5. Star Rating Performance


4-star hotels are the highest-performing segment: 12,034 bookings generating ₹354.84 Million in revenue.
Revenue differences across star ratings are volume-driven, not price-driven — average selling prices are similar across segments.


6. Loyalty & Customer Segments


46.42% of customers have no loyalty tier — representing the largest retention opportunity on the platform.
Loyalty tier breakdown: None (46.42%) → Silver (26.12%) → Gold (17.50%) → Platinum (9.95%).
Customer segment breakdown: Individual (64.17%) → Corporate (24.10%) → Group (11.73%).
OTA skews heavily toward Individual travelers (+7.72pp vs platform), explaining its higher discount dependency and lower repeat rates.


7. Holiday Demand


1,006 bookings (8.38% of Dataset B) were classified as holiday-adjacent (check-in within ±2 days of a public holiday).
Holiday-adjacent bookings show similar booking value (₹31,158 vs ₹31,328 for regular) but higher cancellation risk (22.17% vs 18.91%).
Holiday proximity does not generate a booking value premium — it only adds cancellation risk.
Public holiday data sourced via the Nager.Date Public Holidays API (India, 2024).


8. Revenue Trend


Dataset B shows exponential revenue growth from late 2023 onwards, accelerating sharply from ₹24.6M cumulative through December 2023 to ₹294.9M by December 2024.
April is the peak month for bookings and revenue in Dataset A; the platform otherwise shows stable demand with no strong seasonal troughs.
Average stay length is approximately 4 days (Dataset A) and 2.85–2.90 nights (Dataset B).

## Power BI Dashboard

The final dashboard consists of three interactive report pages designed for different business stakeholders.

### Executive Overview
- Total Revenue
- Total Bookings
- Total Customers
- Average Booking Value
- ADR
- Cancellation Rate
- Revenue by City
- Revenue by Channel

### Revenue & Booking Insights
- Revenue Realization
- Revenue Leakage
- Revenue Trend
- Discount vs Revenue
- Property Type Analysis
- Booking Channel Analysis

### Customer & Operational Insights
- Customer Segments
- Loyalty Tier Analysis
- Guest Review Ratings
- Customer Home City Distribution
- Booking Channel vs Loyalty
- Hotel Rating Analysis

### DAX Measures

More than 35 business measures were created including:

- Revenue Realization %
- Revenue Lost
- Average ADR
- Average Booking Value
- Total Customers
- Average Review
- Coupon Usage
- Time Intelligence
- Running Revenue

### Data Model

The Power BI solution follows a Star Schema architecture:

Fact Bookings

Dim Date

Dim Holiday

Dedicated Measure Table

Relationships optimized for analytical performance.

## Root Cause Summary

#FindingRoot CauseConfidenceRCA-1Travel Agent cancellation rate 27.93%Intermediary relationship reduces customer commitmentHighRCA-2Standard room cancellation rate 23.30%Price-sensitive customers more likely to switch or abandonHighRCA-3Web channel outperforms all othersDirect booking reflects stronger purchase intentHighRCA-4Revenue is volume-driven, not price-drivenStandardized pricing structure across segmentsMediumRCA-54-star properties dominate performanceOptimal affordability-quality balance for broad customer baseMediumRCA-6Lead time does not predict cancellationsCancellation driven by channel and segment factors, not timingHighRCA-7Coupons ineffective for retentionCustomers redeem for monetary benefit, not commitmentMediumRCA-8OTA discounts structurally elevatedOTA customer mix skews Individual (+7.72pp), requiring higher incentivesHighRCA-9Holiday bookings show elevated cancellationHoliday plans are more prone to change than regular travelMedium


## Business Recommendations

PriorityRecommendationEvidenceExpected ImpactHighPromote Direct Web Bookings with exclusive incentivesWeb: lowest cancel rate (17.64%), highest profit (₹104.78M)↓ Cancellations, ↑ MarginHighRestructure OTA coupon program — reduce spend by 50%Coupon users: -13.45% per-room value, ₹4.86M recoverable margin₹4.86M margin recoveryHighReduce Travel Agent dependency; migrate customers to direct channelsTravel Agent cancel rate: 27.93%↓ Revenue leakageHighIntroduce retention measures for Standard Room customers (flex rescheduling, non-refundable discounts)Standard room cancel rate: 23.30%, highest volume segmentRecover portion of ₹179.66M at-risk revenueMediumLaunch tiered loyalty program targeting the 46.42% with no loyalty status46.42% of customers have no tier; coupon users show -2.11pp repeat rate↑ Customer lifetime valueMediumEnforce stricter cancellation policy for holiday-adjacent bookingsHoliday cancel rate 22.17% vs 18.91% regular; no booking value premium↓ Holiday revenue leakageMediumExpand 4-star hotel inventory and prioritize its visibility4-star: 12,034 bookings, ₹354.84M revenue — highest in segment↑ Volume-driven revenueLowMaintain and monitor geographic diversificationRevenue balanced across Chennai, Bangalore, Delhi, Mumbai, Goa, etc.Reduce market concentration risk


## SQL Analysis Highlights

A normalized relational schema was designed to support production-grade data storage and analytical queries:

sql-- 4-table normalized schema
CREATE TABLE customers (customer_id, name, segment, signup_date, home_city, loyalty_tier);
CREATE TABLE properties (property_id, name, city, star_rating, type, total_rooms);
CREATE TABLE bookings   (booking_id, customer_id, property_id, checkin_date, checkout_date,
                         room_type, num_rooms, nights, booking_channel, adr,
                         discount_amount, coupon_code, total_amount, booking_status);
CREATE TABLE reviews    (booking_id, review_rating, review_date);

-- Data integrity constraints
CHECK (checkout_date > checkin_date)
CHECK (num_rooms > 0)
INDEX ON bookings(booking_date)

Key SQL Queries Executed:


DENSE_RANK() over property type to identify the most booked room type per property category → Standard rooms rank #1 across all property types.
Window function cumulative revenue: SUM(realized_revenue) OVER (ORDER BY booking_month) → Tracked exponential revenue growth from Oct 2021 to Dec 2024.



## Project Structure

Hotel_Booking_Analytics/
│
├── README.md
├── FINAL_REPORT.md
├── requirements.txt
├── Hotel_Business_Intelligence.pbix           # 3-page interactive dashboard
├── business_recommendations.md
│
├── dashboard/
│   ├── page 1.png                                # Executive_Overview
│   ├── page 2.png                                # Revenue_Booking_Insights
│   └── page 3.png                                # Customer_Operational_Insights
│ 
├── data/
│   ├── raw/
│   │   ├── hotel_bookings_final.csv              # 30,000 records
│   │   ├── hotel_bookings(1).csv                 # 12,000 records
│   │   └── holiday_calendar.csv                  
│   └── processed/
│       ├── hotel_bookings_clean.csv
│       └── completed_bookings_analysis.csv
│
├── sql/
│   ├── schema.sql                            # Normalized 4-table schema
│   └── queries.sql                           # Window function queries
│
├── notebooks/
│   └── hotel_booking_analysis.ipynb
│
├── src/
│   ├── business_metrics.py
│   ├── cancellation_analysis.py
│   ├── channel_analysis.py
│   ├── revenue_analysis.py
│   ├── profitability_analysis.py
│   ├── seasonality_analysis.py
│   ├── coupon_analysis.py
│   ├── lead_time_analysis.py
│   ├── star_rating_analysis.py
│   ├── customer_analysis.py
│   ├── city_analysis.py
│   ├── visualizations.py
│
├── project/ holiday_tagger/
│       └── holiday_demand_tagger.py          # Nager.Date API integration
│
├── reports/
│   ├── figures/                              # All generated charts
│   └── tables/                              # All CSV summary outputs


Tools & Technologies

CategoryToolsLanguagePython 3.11Data Manipulationpandas, numpyVisualizationmatplotlib, seabornSQLSQLite / PostgreSQL — schema design, window functions, DENSE_RANKFeature Engineeringholidays library, requests (Nager.Date API)DashboardPower BI Desktop (DAX, data modeling, slicers)Notebook EnvironmentJupyter NotebookVersion ControlGit / GitHub


Setup Instructions

bash# 1. Clone the repository
git clone https://github.com/yourusername/Hotel_Booking_Analytics_Combined.git
cd Hotel_Booking_Analytics_Combined

# 2. Create and activate virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run analysis scripts
python src/business_metrics.py
python src/cancellation_analysis.py
python src/holiday_tagger/holiday_demand_tagger.py

# 5. Launch notebooks
jupyter notebook

requirements.txt

pandas==2.1.4
numpy==1.26.2
matplotlib==3.8.2
seaborn==0.13.0
openpyxl==3.1.2
notebook==7.0.6
ipykernel==6.27.1
python-dateutil==2.8.2
holidays==0.41
requests==2.31.0


Conclusion

This combined analysis demonstrates that the platform's most significant profit opportunity lies not in acquiring more bookings, but in improving the quality of existing ones. The Web / Direct channel consistently outperforms intermediaries across every metric. OTA volume is real but structurally expensive — the discount premium and coupon dependency are eroding margin without improving loyalty. Cancellations are concentrated in predictable, manageable segments: Travel Agent bookings, Standard rooms, and holiday windows.

The data makes a clear case: shift acquisition spend toward direct channels, replace blanket coupons with loyalty-linked incentives, and enforce tighter cancellation rules for high-risk windows. These three moves alone have a quantified upside of ₹4.86M+ in recoverable margin and ₹179.66M in at-risk revenue that can be partially retained with targeted intervention.