/*
Schema Design Notes

Normalization:
1. Customer attributes moved to customers table.
2. Property attributes moved to properties table.
3. Booking transactions stored in bookings table.
4. Review information stored separately.

Constraint:
CHECK (checkout_date > checkin_date)

Index:
booking_date indexed for analytical queries.
*/

CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    customer_segment VARCHAR(20) NOT NULL,
    customer_signup_date DATE NOT NULL,
    customer_home_city VARCHAR(50) NOT NULL,
    customer_loyalty_tier VARCHAR(20) NOT NULL
);

CREATE TABLE properties (
    property_id INTEGER PRIMARY KEY,
    property_name VARCHAR(100) NOT NULL,
    property_city VARCHAR(50) NOT NULL,
    property_star_rating INTEGER NOT NULL,
    property_type VARCHAR(30) NOT NULL,
    property_total_rooms INTEGER NOT NULL,

    CHECK (property_total_rooms > 0)
);

CREATE TABLE bookings (
    booking_id INTEGER PRIMARY KEY,

    customer_id INTEGER NOT NULL,
    property_id INTEGER NOT NULL,

    booking_date DATE NOT NULL,
    checkin_date DATE NOT NULL,
    checkout_date DATE NOT NULL,

    room_type VARCHAR(20) NOT NULL,
    num_rooms INTEGER NOT NULL,
    nights INTEGER NOT NULL,

    booking_channel VARCHAR(30) NOT NULL,

    adr DECIMAL(12,2) NOT NULL,
    discount_amount DECIMAL(12,2) NOT NULL,
    coupon_code VARCHAR(20),

    total_amount DECIMAL(12,2) NOT NULL,

    payment_method VARCHAR(30) NOT NULL,
    booking_status VARCHAR(20) NOT NULL,

    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id),

    FOREIGN KEY (property_id)
        REFERENCES properties(property_id),

    CHECK (checkout_date > checkin_date),

    CHECK (num_rooms > 0)
);

CREATE TABLE reviews (
    booking_id INTEGER PRIMARY KEY,

    review_rating DECIMAL(4,2),
    review_date DATE,

    FOREIGN KEY (booking_id)
        REFERENCES bookings(booking_id)
);

CREATE INDEX idx_booking_date
ON bookings(booking_date);