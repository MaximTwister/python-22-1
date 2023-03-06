INSERT INTO customers (customer_name, email)
VALUES
  ('John Smith', 'john@gmail.com'),
  ('Jane Doe', 'jane@gmail.com'),
  ('Bob Johnson', 'bob@gmail.com'),
  ('Alice Lee', 'alice@gmail.com'),
  ('David Davis', 'david@gmail.com'),
  ('Emily Brown', 'emily@gmail.com'),
  ('George Williams', 'george@gmail.com'),
  ('Hannah Miller', 'hannah@gmail.com'),
  ('Isaac Wilson', 'isaac@gmail.com'),
  ('Julia Garcia', 'julia@gmail.com'),
  ('Kevin Jones', 'kevin@gmail.com'),
  ('Laura Martinez', 'laura@gmail.com'),
  ('Michael Rodriguez', 'michael@gmail.com'),
  ('Natalie Davis', 'natalie@gmail.com'),
  ('Oliver Robinson', 'oliver@gmail.com'),
  ('Penelope Taylor', 'penelope@gmail.com'),
  ('Quinn Johnson', 'quinn@gmail.com'),
  ('Rachel Baker', 'rachel@gmail.com'),
  ('Samantha Scott', 'samantha@gmail.com'),
  ('Thomas Clark', 'thomas@gmail.com');

INSERT INTO main_courses (main_course_name, price)
VALUES
  ('Hamburger', 4.99),
  ('Cheeseburger', 5.49),
  ('Hot dog', 3.99),
  ('Chicken nuggets', 6.99),
  ('Fish and chips', 7.99),
  ('Grilled chicken sandwich', 6.49),
  ('BBQ pork sandwich', 7.49),
  ('Meatballs', 6.99),
  ('Spicy turkey sandwich', 5.99),
  ('Taco salad', 8.99);

INSERT INTO drinks (drink_name, price)
VALUES
  ('Coca-Cola', 1.99),
  ('Sprite', 1.99),
  ('Fanta', 1.99),
  ('Dr. Pepper', 2.49),
  ('Lager beer', 2.49),
  ('Pilsner beer', 2.00),
  ('Iced tea', 2.49),
  ('Orange juice', 2.99),
  ('Apple juice', 2.99),
  ('Milkshake', 3.99);

INSERT INTO meals (main_course_id, drink_id)
SELECT main_courses.id, drinks.id
FROM main_courses
CROSS JOIN drinks;

INSERT INTO orders (order_date, customer_id, order_sum)
SELECT
    current_date - CAST(random() * 360 AS INTEGER) + interval '1 day' AS order_date,
    CAST((random() * 19 + 1) AS INTEGER) AS customer_id,
    CAST((random() * 100 + 10) AS NUMERIC(10, 2)) AS order_sum
FROM generate_series(1, 1000);

-- Option via CROSS JOIN LATERAL
INSERT INTO order_meal (order_id, meal_id, portions)
SELECT
    o.id AS order_id,
    selected_random_meal.id AS meal_id,
    trunc(random() * 3 + 1) as portions
FROM orders AS o
CROSS JOIN LATERAL (
    SELECT * FROM meals AS m
        WHERE m.id NOT IN (
            SELECT meal_id
            FROM order_meal
            WHERE order_id = o.id
    )
    ORDER BY random()
    LIMIT 1
    ) as selected_random_meal;

-- Option via SELECT subquery
INSERT INTO order_meal (order_id, meal_id, portions)
SELECT
    o.id AS order_id,
    (SELECT id FROM meals AS selected_random_meal
        WHERE selected_random_meal.id NOT IN (
            SELECT meal_id
            FROM order_meal
            WHERE order_id = o.id
        )
        ORDER BY random()
        LIMIT 1
    ) as meal_id,
    trunc(random() * 3 + 1) as portions
FROM orders AS o;
