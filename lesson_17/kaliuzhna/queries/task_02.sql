--2. List all customers who have ordered a particular main course.

DROP TYPE IF EXISTS CUSTOMER_TYPE;
CREATE TYPE CUSTOMER_TYPE AS (id INTEGER);

DO $$
DECLARE
    main_course VARCHAR(50) := 'Cheeseburger';
    customers CUSTOMER_TYPE[];
    customer_id CUSTOMER_TYPE;

BEGIN
 FOR customer_id IN
	select distinct(c.id)
	FROM main_courses mc
	join meals m on mc.id = m.main_course_id
	join order_meal om on m.id = om.meal_id
	join orders o on om.order_id = o.id
	join customers c on c.id = o.customer_id
	WHERE mc.main_course_name = main_course

LOOP
    customers := array_append(customers, customer_id);
END LOOP;

RAISE NOTICE 'CUSTOMERS: %', customers;
END;
$$;