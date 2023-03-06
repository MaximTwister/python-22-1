-- Create `fastfood` database section
-- hiqcwovy
-- DROP DATABASE IF EXISTS fastfood;
-- CREATE DATABASE fastfood;

DROP TABLE IF EXISTS customers CASCADE;
CREATE TABLE customers(
    id SERIAL PRIMARY KEY,
    customer_name VARCHAR(50),
    email VARCHAR(50)
);

DROP TABLE IF EXISTS main_courses CASCADE;
CREATE TABLE main_courses(
    id SERIAL PRIMARY KEY,
    main_course_name VARCHAR(50),
    price NUMERIC(10, 2)
);

DROP TABLE IF EXISTS drinks CASCADE;
CREATE TABLE drinks(
    id SERIAL PRIMARY KEY,
    drink_name VARCHAR(50),
    price NUMERIC(10, 2)
);

DROP TABLE IF EXISTS meals CASCADE;
CREATE TABLE meals(
    id SERIAL PRIMARY KEY,
    main_course_id INTEGER REFERENCES main_courses(id),
    drink_id INTEGER REFERENCES drinks(id)
);

DROP TABLE IF EXISTS orders CASCADE;
CREATE TABLE orders(
    id SERIAL PRIMARY KEY,
    order_date DATE DEFAULT NOW(),
    customer_id INTEGER REFERENCES customers(id),
    order_sum NUMERIC(10, 2)
);

DROP TABLE IF EXISTS order_meal CASCADE;
CREATE TABLE order_meal(
    order_id INTEGER REFERENCES orders(id),
    meal_id INTEGER REFERENCES meals(id),
    PRIMARY KEY(order_id, meal_id),
    portions INTEGER DEFAULT 1
);

DROP TABLE IF EXISTS discounts CASCADE;
CREATE TABLE discounts(
    id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(id),
    meal_id INTEGER REFERENCES meals(id),
    percents NUMERIC(10, 2),
    period DATERANGE
);
