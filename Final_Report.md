Hotel Booking Analytics — Final Report

Combined Analysis: Dataset A (30,000 Bookings) + Dataset B (12,000 Bookings)


1. Executive Summary

This report presents the findings of a full-stack data analytics engagement on hotel booking transaction data from an online travel platform. Two datasets totaling 42,000 booking records were analyzed independently and then synthesized to produce a unified set of insights and strategic recommendations.

Dataset A (30,000 records, 24 features) covers channel performance, cancellation behavior, room type and star rating analysis, profitability metrics, and seasonality patterns.

Dataset B (12,000 records) extends the analysis into discount strategy, OTA coupon economics, customer loyalty tier distribution, holiday demand feature engineering, and SQL schema design with window function queries.

Together, they enable a complete picture of where the platform is generating value, where it is leaking margin, and what interventions will have the largest measurable impact.


1.1 Top-Line Business Metrics

Dataset A

MetricValueTotal Bookings30,000Confirmed Bookings21,672Cancelled Bookings6,070Failed Bookings2,258Cancellation Rate20.23%Total Revenue₹885.14 MillionTotal Profit (Markup)₹208.90 MillionProfit Margin23.60%Revenue at Risk (Cancellations)₹179.66 MillionTotal Refunds Issued₹9.63 Million

Dataset B

MetricValueTotal Bookings12,000Unique Customers800Unique Properties60Completed Bookings9,333 (77.78%)Cancelled Bookings2,302 (19.18%)No-Show Bookings365 (3.04%)Gross (Booked) Revenue₹375.76 MillionRealized Revenue₹294.86 MillionPlatform Avg. Discount Intensity5.33%OTA Discount Intensity7.30%OTA Discount Premium vs Platform+1.97 percentage pointsEstimated Recoverable Margin₹4.86 Million


1.2 Critical Findings at a Glance


Direct / Web channel has the lowest cancellation rate (17.64%) and highest profit (₹104.78M). It is the platform's most valuable acquisition source.
OTA operates at a 1.97pp discount premium over the platform average, yet this is not justified by customer loyalty mix or geographic mix — it reflects a structurally price-sensitive customer base.
Coupon users generate 13.45% less per-room revenue and show lower repeat booking rates (-2.11pp). Promotions attract transactions, not loyalty.
₹4.86 Million in margin can be recovered by reducing OTA coupon spend by 50%, with only marginal cancellation risk.
Travel Agent bookings cancel at 27.93% — the highest of any channel — creating the largest single source of revenue leakage.
46.42% of customers have no loyalty tier, representing the largest addressable retention gap on the platform.
Holiday-adjacent bookings (8.38% of Dataset B) cancel at 22.17% vs 18.91% for regular bookings, but generate no booking value premium to compensate.



2. Data Overview & Quality

2.1 Dataset A — Structure


Records: 30,000 booking transactions
Features: 24 variables covering customer, property, booking, and financial dimensions


Key fields: booking_channel, booking_status, room_type, star_rating, selling_price, costprice, markup, refund_amount, coupon_used, customer_id, property_id, booking_date, check_in_date, check_out_date

2.2 Dataset B — Structure & Quality Audit


Records: 12,000 booking transactions
Unique Customers: 800 | Unique Properties: 60


Data quality issues identified and resolved in Dataset B:

IssueRecords AffectedResolutionZero-room bookingsFlagged in zero_rooms.csvExcluded from revenue analysisInvalid stays (checkout ≤ checkin)Flagged in invalid_stays.csvExcluded from stay-length metricsBookings before customer signupFlagged in Booking_Before_Signup.csvExcluded from loyalty analysisSchema constraint addedCHECK (checkout_date > checkin_date)Prevents future invalid records

2.3 Normalized Relational Schema (Dataset B)

A production-ready 4-table normalized schema was designed to support the analytical workload:

sqlCREATE TABLE customers (
    customer_id       INTEGER PRIMARY KEY,
    customer_name     VARCHAR(100) NOT NULL,
    customer_segment  VARCHAR(20)  NOT NULL,  -- Individual / Corporate / Group
    customer_signup_date DATE      NOT NULL,
    customer_home_city   VARCHAR(50) NOT NULL,
    customer_loyalty_tier VARCHAR(20) NOT NULL -- None / Silver / Gold / Platinum
);

CREATE TABLE properties (
    property_id          INTEGER PRIMARY KEY,
    property_name        VARCHAR(100) NOT NULL,
    property_city        VARCHAR(50)  NOT NULL,
    property_star_rating INTEGER      NOT NULL,
    property_type        VARCHAR(30)  NOT NULL, -- Budget / Mid-Range / Premium / Luxury
    property_total_rooms INTEGER      NOT NULL,
    CHECK (property_total_rooms > 0)
);

CREATE TABLE bookings (
    booking_id       INTEGER PRIMARY KEY,
    customer_id      INTEGER NOT NULL,
    property_id      INTEGER NOT NULL,
    booking_date     DATE    NOT NULL,
    checkin_date     DATE    NOT NULL,
    checkout_date    DATE    NOT NULL,
    room_type        VARCHAR(20)    NOT NULL,
    num_rooms        INTEGER        NOT NULL,
    nights           INTEGER        NOT NULL,
    booking_channel  VARCHAR(30)    NOT NULL,
    adr              DECIMAL(12,2)  NOT NULL,
    discount_amount  DECIMAL(12,2)  NOT NULL,
    coupon_code      VARCHAR(20),
    total_amount     DECIMAL(12,2)  NOT NULL,
    payment_method   VARCHAR(30)    NOT NULL,
    booking_status   VARCHAR(20)    NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (property_id) REFERENCES properties(property_id),
    CHECK (checkout_date > checkin_date),
    CHECK (num_rooms > 0)
);

CREATE TABLE reviews (
    booking_id     INTEGER PRIMARY KEY,
    review_rating  DECIMAL(4,2),
    review_date    DATE,
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id)
);

CREATE INDEX idx_booking_date ON bookings(booking_date);

Design rationale: Separating customers, properties, bookings, and reviews into distinct tables reduces data redundancy, enforces referential integrity, and enables scalable analytical queries. The booking_date index directly accelerates the monthly revenue window function queries used in the SQL analysis section.


3. Channel Performance Analysis

3.1 Dataset A — Channel Breakdown

ChannelBookingsRevenueProfitCancellation RateWeb15,001₹443.99M₹104.78M17.64%Mobile App~7,500 (est.)——21.56%Travel Agent———27.93%

Key finding: The Web channel accounts for approximately 50% of all bookings and generates the highest revenue, the highest profit, and the lowest cancellation rate simultaneously. This is the most important channel-level finding: volume, profitability, and quality are all concentrated in the same place.

Travel Agent bookings sit at the opposite extreme — highest cancellation rate, lowest channel efficiency. The likely mechanism is intermediary distance: customers booking through agents have weaker direct commitment to the platform and face fewer friction costs to cancel.

3.2 Dataset B — Channel Discount Decomposition

ChannelCompleted BookingsGross RevenueDiscount AmountRealized RevenueDiscount IntensityGap vs PlatformOTA3,180₹106.92M₹7.81M₹99.11M7.30%+1.97ppCorporate Portal2,457₹83.59M₹3.46M₹80.12M4.14%-1.19ppDirect Website1,748₹57.38M₹2.52M₹54.86M4.39%-0.94ppTravel Agent1,948₹63.57M₹2.80M₹60.76M4.41%-0.92pp

Platform average discount intensity: 5.33%

OTA is the only channel above the platform average. The 1.97pp premium over the platform average represents a structural discount burden that Corporate Portal, Direct Website, and Travel Agent do not carry.

3.3 Why OTA Discounts Are Elevated — Composition Analysis

Three hypotheses were tested to explain OTA's elevated discount intensity:

HypothesisFindingConclusionOTA attracts lower-loyalty customersOTA loyalty mix nearly identical to platformNot the causeOTA is concentrated in higher-cost citiesOTA city mix nearly identical to platformNot the causeOTA attracts more price-sensitive customer segmentsOTA: Individual +7.72pp vs platform averageConfirmed — structural cause

OTA's customer base skews 7.72 percentage points more toward Individual travelers than the platform average. Individual travelers are more price-sensitive and respond more strongly to discount incentives — meaning OTA's discount premium is a structural feature of who it attracts, not an operational choice that can be easily corrected without changing the channel's customer mix.

Channel + Segment cross-tab (OTA vs Platform):

SegmentOTA %Platform %DifferenceIndividual71.82%64.10%+7.72ppCorporate14.09%24.08%-9.99ppGroup14.09%11.83%+2.26pp

The implication is clear: efforts to reduce OTA discounts without a customer acquisition strategy shift will face resistance, because the OTA audience inherently demands higher incentives than the platform average.


4. Coupon & Discount Effectiveness Analysis

4.1 Coupon Impact on Key Metrics

MetricCoupon UsersNon-Coupon UsersDifferenceCancellation Rate21.67%22.28%-0.61ppAvg Per-Room Amount₹20,087₹23,210-13.45%Repeat Booking Rate73.99%76.10%-2.11pp

Interpretation:

Coupons reduce cancellations by less than 1 percentage point — a marginal impact that is unlikely to justify the revenue cost. More critically, coupon users generate 13.45% less revenue per room and are 2.11 percentage points less likely to return for a repeat booking. This pattern is the opposite of what a healthy promotional program should produce. Promotions are being used by a customer segment that is price-motivated, not loyalty-motivated.

4.2 OTA-Specific Coupon Economics


Dataset B had 4,128 coupon bookings and 7,872 non-coupon bookings (34.4% coupon penetration).
OTA channel carries the highest discount intensity (7.30%) and the highest coupon concentration.
Estimated recoverable margin from reducing OTA coupon spend by 50%: ₹4.86 Million.


This recovery assumes the marginal cancellation risk from coupon reduction is absorbed without proportional revenue loss — supported by the finding that coupons improve cancellation rates by only 0.61pp.


5. Cancellation Analysis

5.1 Cancellation by Channel

ChannelCancellation RateTravel Agent27.93%Mobile App21.56%Overall Platform20.23%Web17.64%

The 10.29pp spread between Travel Agent (worst) and Web (best) represents a substantial quality gap that is directly actionable through channel mix strategy.

5.2 Cancellation by Room Type

Room TypeCancellation RateStandard23.30%Suite17.98%Deluxe16.02%

Standard rooms are the highest-volume room type (49.49% of bookings in Dataset B; similarly dominant in Dataset A) and carry the highest cancellation rate. The combination means Standard room cancellations drive the largest absolute revenue leakage of any single segment.

5.3 Cancellation by Booking Lead Time

StatusAverage Lead TimeCancelled30.21 daysConfirmed30.38 daysFailed30.43 days

Lead time is not a predictor of cancellation. The near-identical averages across all booking statuses rule out early/late booking timing as a root cause. Cancellation is driven by channel and customer segment factors, not by when the booking was made. This finding is important because it rules out a commonly assumed intervention (targeting long-lead bookings for re-engagement) as ineffective.

5.4 Holiday-Adjacent Cancellation Behavior

Using a custom Python holiday tagger integrated with the Nager.Date Public Holidays API (India, 2024), bookings were classified as holiday-adjacent if check-in fell within ±2 days of a public holiday.

SegmentBookingsAvg Booking ValueAvg Stay LengthCancellation RateRegular10,994₹31,3282.85 nights18.91%Holiday Adjacent1,006 (8.38%)₹31,1582.90 nights22.17%

Holiday-adjacent bookings are more likely to cancel (+3.26pp) but generate no material booking value premium (₹170 lower per booking). The platform absorbs extra cancellation risk around holidays without receiving a revenue benefit in return. This makes holiday windows a clear candidate for stricter cancellation policy enforcement.


6. Room Type & Property Analysis

6.1 Room Type Distribution (Dataset B)

Room TypeCount% of BookingsStandard5,93949.49%Deluxe4,28935.74%Suite1,77214.77%

6.2 Property Type Distribution (Dataset B)

Property TypeCount% of BookingsMid-Range4,74939.57%Budget3,77231.43%Premium2,08617.38%Luxury1,39311.61%

6.3 Most Booked Room Type by Property Category (SQL: DENSE_RANK)

Using a DENSE_RANK() window function over completed bookings partitioned by property type, Standard rooms rank #1 in most booked room type across all property categories. This confirms that Standard room demand is not isolated to budget properties — it is the dominant room type across the property portfolio, which amplifies the business impact of its elevated cancellation rate.

sqlWITH room_type_counts AS (
    SELECT
        p.property_type,
        b.room_type,
        COUNT(*) AS completed_bookings,
        DENSE_RANK() OVER (
            PARTITION BY p.property_type
            ORDER BY COUNT(*) DESC
        ) AS room_rank
    FROM bookings b
    INNER JOIN properties p ON b.property_id = p.property_id
    WHERE b.booking_status = 'Completed'
    GROUP BY p.property_type, b.room_type
)
SELECT property_type, room_type, completed_bookings
FROM room_type_counts
WHERE room_rank = 1
ORDER BY property_type;

6.4 Star Rating Performance (Dataset A)

Star RatingBookingsRevenue4-star12,034₹354.84 Million3-star——5-star——

4-star properties dominate on both volume and revenue. Revenue differences across star ratings are volume-driven rather than price-driven — average selling prices are relatively uniform across star categories, confirming that platform pricing is standardized rather than premium-differentiated.


7. Customer & Loyalty Analysis

7.1 Customer Segment Distribution (Dataset B)

SegmentCount%Individual7,70064.17%Corporate2,89224.10%Group1,40811.73%

7.2 Loyalty Tier Distribution (Dataset B)

TierCount%None5,57146.42%Silver3,13526.12%Gold2,10017.50%Platinum1,1949.95%

46.42% of the customer base carries no loyalty tier. This is the single largest addressable retention segment. Combined with the finding that coupon users (who are more likely to be tier-less, transactional customers) show lower repeat rates, it creates a clear mandate: replace coupon spend with loyalty program investment targeting the None tier.

Dataset A independently corroborated this with 499 unique customers averaging 60+ bookings each — a highly engaged repeat base that is already behaving like loyalty customers without a formal program to recognize or reward them.


8. Seasonality & Revenue Trend Analysis

8.1 Monthly Revenue Trend (Dataset A)


April recorded the highest booking volume and revenue.
Booking demand remained relatively stable across remaining months with no sharp seasonal troughs.
Average stay length: approximately 4 days.


8.2 Cumulative Revenue Growth (Dataset B — Window Function)

Using SUM(realized_revenue) OVER (ORDER BY booking_month), the cumulative revenue trajectory shows exponential growth acceleration:

PeriodCumulative Realized RevenueThrough Dec 2022₹1.78 MillionThrough Dec 2023₹24.59 MillionThrough Apr 2024₹117.95 MillionThrough Dec 2024₹294.86 Million

The platform experienced a step-change growth inflection in late 2023, with revenue accelerating sharply from Q4 2023 through 2024. This growth trend underscores the strategic importance of margin protection: as absolute revenue scales, the cost of structural inefficiencies (OTA discount premium, coupon erosion, Travel Agent cancellations) scales proportionally.

sqlWITH monthly_revenue AS (
    SELECT
        DATE_TRUNC('month', booking_date) AS booking_month,
        SUM(total_amount) AS realized_revenue
    FROM bookings
    WHERE booking_status = 'Completed'
    GROUP BY DATE_TRUNC('month', booking_date)
)
SELECT
    booking_month,
    realized_revenue,
    SUM(realized_revenue) OVER (ORDER BY booking_month) AS cumulative_revenue
FROM monthly_revenue
ORDER BY booking_month;


9. Root Cause Analysis

RCA-1: Travel Agent Channel — Highest Cancellation Rate (27.93%)

Evidence: Travel Agent cancellation rate is 27.93% vs 17.64% for Web — a 10.29pp gap.

Root cause: Indirect booking relationships reduce customer commitment. Customers who book through agents have weaker direct engagement with the platform and lower psychological ownership of the booking decision. This produces both higher cancellation frequency and lower booking quality overall.

Confidence: High


RCA-2: Standard Rooms — Highest Room-Type Cancellation Rate (23.30%)

Evidence: Standard: 23.30% | Suite: 17.98% | Deluxe: 16.02%.

Root cause: Standard room customers are more price-sensitive and more likely to hold multiple options, switch to competing offers, or cancel under minor financial uncertainty. The lower price point reduces perceived switching cost.

Confidence: High


RCA-3: Web Channel — Consistent Outperformance Across All Metrics

Evidence: Highest volume (15,001 bookings), revenue (₹443.99M), profit (₹104.78M), and lowest cancellation rate (17.64%) simultaneously.

Root cause: Direct website booking reflects stronger purchase intent. Customers who seek out and use the platform's own interface have already passed a higher commitment threshold than customers who arrive through intermediaries.

Confidence: High


RCA-4: Revenue is Volume-Driven, Not Price-Driven

Evidence: Average selling prices remain highly similar across channels and star categories. Revenue differences track booking volume, not pricing differences.

Root cause: The platform operates with a standardized pricing structure rather than segment- or channel-specific premium pricing.

Implication: The primary lever for revenue growth is increasing booking volume and confirmation rates, not raising prices.

Confidence: Medium


RCA-5: OTA Discount Premium Explained by Customer Composition

Evidence: OTA discount intensity is 7.30% vs 5.33% platform average (+1.97pp). Loyalty mix and city mix between OTA and platform are nearly identical. Individual traveler share on OTA is +7.72pp vs platform.

Root cause: OTA systematically attracts more price-sensitive Individual travelers. This is a customer acquisition structural issue, not a negotiation or operations issue. Reducing OTA discounts without addressing the underlying customer mix will face resistance.

Confidence: High


RCA-6: Lead Time Does Not Predict Cancellation

Evidence: Cancelled (30.21 days), Confirmed (30.38 days), Failed (30.43 days) — nearly identical averages across all statuses.

Root cause: Cancellation behavior is driven by channel and customer segment characteristics, not by when the booking was placed. Early re-engagement programs targeting long-lead bookings are unlikely to reduce cancellations meaningfully.

Confidence: High


RCA-7: Coupons Attract Transactions, Not Loyalty

Evidence: Coupon users show -13.45% per-room value, -2.11pp repeat rate, and only -0.61pp cancellation rate reduction.

Root cause: Customers redeem coupons for monetary benefit in a specific transaction. The incentive does not create ongoing platform preference or reduce cancellation commitment. Coupon-motivated customers are more transactional than loyalty-motivated customers, as evidenced by lower repeat booking rates.

Confidence: Medium


RCA-8: Holiday Bookings Carry Elevated Risk Without Compensating Value

Evidence: Holiday-adjacent cancel rate: 22.17% vs regular 18.91%. Booking value: ₹31,158 vs ₹31,328.

Root cause: Holiday travel plans are more fluid and subject to change than regular travel. Customers booking near public holidays may be exploring options rather than committing, producing higher cancellation rates. The platform captures no booking value premium that would compensate for this risk.

Confidence: Medium


10. Business Recommendations

Priority 1 (High): Promote Direct Web Bookings

Evidence: Web channel: 17.64% cancel rate, ₹443.99M revenue, ₹104.78M profit.

Actions:


Introduce web-exclusive discounts not available on OTA or Travel Agent channels
Build loyalty point multipliers for direct bookings
Run marketing campaigns highlighting direct booking benefits (price match, flexible cancellation, loyalty rewards)


Expected impact: Lower platform-wide cancellation rate; higher per-booking margin; reduced intermediary dependency.


Priority 2 (High): Restructure OTA Coupon Strategy

Evidence: Coupon users generate -13.45% per-room value; ₹4.86M estimated recoverable margin from 50% OTA coupon reduction; -2.11pp repeat rate for coupon users.

Actions:


Reduce blanket OTA coupon distribution by 50%
Redirect coupon budget toward loyalty-linked incentives (Silver → Gold tier upgrade offers)
Monitor OTA cancellation rate for 60 days post-change to confirm marginal risk (expected: +0.61pp, manageable)


Expected impact: ₹4.86M margin recovery; improvement in coupon user repeat rate over time as program shifts toward loyal customers.


Priority 3 (High): Reduce Travel Agent Dependency

Evidence: Travel Agent cancel rate: 27.93% — 10.29pp above Web.

Actions:


Migrate existing Travel Agent customers to direct platform accounts with an incentive (first booking discount via app or web)
Introduce agent performance monitoring with volume-linked commission adjustments for agents above threshold cancellation rates
Reduce marketing investment in agent acquisition


Expected impact: Reduction in platform-wide cancellation rate; lower revenue leakage from uncompleted bookings.


Priority 4 (High): Reduce Standard Room Cancellations

Evidence: Standard rooms: 23.30% cancel rate, 49.49% of all bookings, largest single source of cancellation volume.

Actions:


Introduce a non-refundable Standard rate with a 5–10% discount for customers willing to commit upfront
Offer flexible rescheduling (date change without penalty) as an alternative to cancellation
Provide loyalty points for confirmed Standard room stays as a retention incentive


Expected impact: Even a 3–4pp reduction in Standard room cancellation rate across 30,000 bookings recovers several hundred cancellations and meaningful realized revenue.


Priority 5 (Medium): Launch Structured Loyalty Program

Evidence: 46.42% of customers have no loyalty tier; coupon users show -2.11pp repeat rate; Dataset A shows 499 customers averaging 60+ bookings each.

Actions:


Create an onboarding incentive for None-tier customers to register for the loyalty program (first Silver tier benefit at signup)
Establish clear tier thresholds and benefits visible at checkout
Replace some coupon spend with loyalty point rewards for completed bookings


Expected impact: Improvement in the 46.42% no-tier customer segment's repeat booking rate; shift from transactional to relationship-based engagement.


Priority 6 (Medium): Enforce Holiday-Period Cancellation Policy

Evidence: Holiday-adjacent cancel rate 22.17% vs 18.91% regular; no booking value premium.

Actions:


Reduce free-cancellation window from 48 hours to 24 hours for bookings with check-in within ±2 days of a public holiday
Add a non-refundable holiday supplement option with a modest discount for customers willing to commit
Surface holiday-period policy clearly at checkout to set expectations


Expected impact: Reduction in holiday-adjacent cancellation rate; recovery of at-risk revenue during high-demand windows.


Priority 7 (Medium): Expand 4-Star Hotel Inventory

Evidence: 4-star properties: 12,034 bookings, ₹354.84M revenue — highest in both metrics.

Actions:


Prioritize new property onboarding in the 4-star segment
Improve 4-star property visibility in search and recommendation algorithms
Build exclusive inventory deals with top-performing 4-star properties


Expected impact: Volume-driven revenue growth in the platform's strongest-performing segment.


Priority 8 (Low): Maintain Geographic Diversification

Evidence: Revenue contribution is balanced across Chennai, Bangalore, Delhi, Mumbai, Goa, Kochi, Pune, Udaipur, Jaipur, and Manali. No single city exceeds 12% of OTA bookings.

Actions:


Continue expanding city coverage without concentrating investment in any single market
Monitor city-level cancellation rates for emerging concentration risk


Expected impact: Reduced market concentration risk; stable revenue base across demand cycles.


11. Summary of Recommendations

PriorityRecommendationKey MetricExpected ImpactHighPromote Direct Web BookingsWeb cancel rate: 17.64%↓ Cancellations, ↑ MarginHighRestructure OTA Coupon Strategy-13.45% per-room value from coupons₹4.86M margin recoveryHighReduce Travel Agent DependencyTravel Agent cancel rate: 27.93%↓ Revenue leakageHighReduce Standard Room CancellationsStandard cancel rate: 23.30%, 49.49% of bookingsRecover at-risk revenueMediumLaunch Structured Loyalty Program46.42% customers with no tier↑ Repeat rate, ↑ LTVMediumEnforce Holiday Cancellation PolicyHoliday cancel rate: 22.17%, no value premium↓ Holiday leakageMediumExpand 4-Star Inventory4-star: highest volume and revenue↑ Volume-driven growthLowMaintain Geographic DiversificationRevenue balanced across 10+ cities↓ Concentration risk


12. Conclusion

The platform is fundamentally healthy — ₹885M+ in revenue across Dataset A, a 23.60% profit margin, and exponential growth through 2024. The strategic risk is not a revenue problem; it is a margin and quality problem concentrated in specific, identifiable segments.

Three structural issues dominate the findings across both datasets:

First, the channel mix is not optimized. Web / Direct channels deliver the best outcomes on every dimension, but OTA and Travel Agent channels account for over 50% of bookings. Shifting even 10–15% of volume from these intermediary channels to direct channels would improve cancellation rates and margin simultaneously.

Second, the promotion strategy is misaligned. Coupons are funding transactional customers who generate less value and repeat less. The ₹4.86M in recoverable margin from OTA coupon rationalization is a concrete, low-risk starting point for reallocation toward loyalty investment — where the platform's 46.42% no-tier customer base represents a large, underactivated retention opportunity.

Third, cancellation risk is concentrated in predictable segments — Travel Agent, Standard rooms, and holiday windows — that can be addressed with targeted policy interventions rather than platform-wide changes. Implementing stricter cancellation terms for these specific risk segments is a more efficient and less disruptive approach than broad policy changes.

The data is clear: the platform does not need more bookings to grow profitability. It needs better bookings — higher-quality, lower-cancellation, direct-channel bookings from customers engaged in a loyalty program that rewards commitment rather than discounts.


13. Appendix

13.1 Visualizations Reference (Dataset A)


Booking Volume by Channel
Revenue by Channel
Cancellation Rate by Channel
Cancellation Rate by Room Type
Revenue by Star Rating
Monthly Revenue Trend
Booking Status Distribution
Profit Contribution by Channel


13.2 Visualizations Reference (Dataset B)


Coupon vs No-Coupon Booking Behavior (cancellation rate, per-room value, repeat rate)
Holiday vs Regular Booking Comparison
Discount Distribution by Channel
Discount Intensity by Channel


13.3 SQL Queries Reference


schema.sql — Normalized 4-table relational schema with constraints and indexes
queries.sql — B-Q1 (DENSE_RANK room type by property) and B-Q2 (cumulative revenue window function)


13.4 Feature Engineering Reference


holiday_demand_tagger.py — Fetches India public holidays from Nager.Date API; creates days_from_holiday and holiday_adjacent features; classifies bookings with check-in within ±2 days as holiday-adjacent.


13.5 Tools & Technologies

LayerToolLanguagePython 3.11Datapandas, numpyVisualizationmatplotlib, seabornSQLSchema design, window functions, DENSE_RANKFeature Engineeringrequests, python-dateutil (Nager.Date API)DashboardPower BI Desktop (DAX, data modeling)EnvironmentJupyter Notebook, venv