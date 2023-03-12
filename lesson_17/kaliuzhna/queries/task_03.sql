--3. Find the most popular meal (pair of main_course + drink) among our customers (during all the period of time) and put 10% discount on that meal for today.

DROP TYPE IF EXISTS CUSTOMER_TYPE;
CREATE TYPE CUSTOMER_TYPE AS (id INTEGER);

DO $$
DECLARE
    top_meals CUSTOMER_TYPE[];
    top_meal_id CUSTOMER_TYPE;
    discount NUMERIC := 10.0;
    order_date date := current_date;
BEGIN
    FOR top_meal_id in
    select meal_id
    from ( select meal_id,
           num,
           DENSE_RANK() OVER (ORDER BY num desc) AS DENSE_RANK
           FROM (SELECT om.meal_id,
                count(om.meal_id) as num
                FROM order_meal om
                GROUP BY om.meal_id
               ORDER BY count(om.meal_id)) dr) a
     where dense_rank  = 1

    LOOP
        top_meals := array_append(top_meals, top_meal_id);
    END LOOP;

    RAISE NOTICE 'the most popular meals: %', top_meals;

    INSERT INTO discounts (meal_id, percents, period)
        SELECT DISTINCT meal_id, discount, daterange(current_date, current_date, '[]')
        from ( select meal_id,
           num,
           DENSE_RANK() OVER (ORDER BY num desc) AS DENSE_RANK
           FROM (SELECT om.meal_id,
                count(om.meal_id) as num
                FROM order_meal om
                GROUP BY om.meal_id
               ORDER BY count(om.meal_id)) dr) a
           where dense_rank  = 1;
END;
$$;