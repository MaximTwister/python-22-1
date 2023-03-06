-- 6.1 Find the top 5 customers with the highest total order sum price
-- 6.2 Give them 25% discount for this month for all meal types.

DROP TYPE IF EXISTS CUSTOMER_TYPE;
CREATE TYPE CUSTOMER_TYPE AS (id INTEGER);

DO $$
DECLARE
    top_five_customers CUSTOMER_TYPE[];
    top_customer_id CUSTOMER_TYPE;
    discount NUMERIC := 25.0;
    customers_amount INTEGER := 5;
BEGIN
    FOR top_customer_id IN
        SELECT customer_id
        FROM orders
        GROUP BY customer_id
        ORDER BY SUM(order_sum)
        LIMIT customers_amount
    LOOP
        top_five_customers := array_append(top_five_customers, top_customer_id);
    END LOOP;

    RAISE NOTICE 'TOP FIVE CUSTOMERS: %', top_five_customers;

    INSERT INTO discounts (customer_id, percents, period)
        SELECT DISTINCT customer_id, discount, daterange(current_date, (current_date + interval '1 month')::DATE, '[]')
        FROM orders
        WHERE customer_id IN (
            SELECT customer_id FROM orders
            GROUP BY customer_id
            ORDER BY SUM(order_sum)
            LIMIT customers_amount
        );
END;
$$;
