-- ==================================================
-- B-Q1
-- For each property type, find the room type with the
-- most Completed bookings using DENSE_RANK()
-- ==================================================

WITH room_type_counts AS (

    SELECT
        p.property_type,
        b.room_type,
        COUNT(*) AS completed_bookings,

        DENSE_RANK() OVER (
            PARTITION BY p.property_type
            ORDER BY COUNT(*) DESC
        ) AS room_rank

    FROM bookings b

    INNER JOIN properties p
        ON b.property_id = p.property_id

    WHERE b.booking_status = 'Completed'

    GROUP BY
        p.property_type,
        b.room_type
)

SELECT
    property_type,
    room_type,
    completed_bookings

FROM room_type_counts

WHERE room_rank = 1

ORDER BY property_type;

-- ==================================================
-- B-Q2
-- Monthly Realized Revenue and Cumulative Revenue
-- ==================================================

WITH monthly_revenue AS (

    SELECT
        DATE_TRUNC('month', booking_date) AS booking_month,
        SUM(total_amount) AS realized_revenue

    FROM bookings

    WHERE booking_status = 'Completed'

    GROUP BY
        DATE_TRUNC('month', booking_date)

)

SELECT
    booking_month,
    realized_revenue,

    SUM(realized_revenue) OVER (
        ORDER BY booking_month
    ) AS cumulative_revenue

FROM monthly_revenue

ORDER BY booking_month;