DROP DATABASE IF EXISTS fastfood;


CREATE DATABASE fastfood;

/* \c fastfood*/

/*customers_customer_id_seq
main_courses_main_course_id_seq
drinks_drink_id_seq*/

CREATE TABLE customers (customer_id SERIAL PRIMARY KEY, name VARCHAR (50) NOT NULL, mail VARCHAR (50) NULL, phone VARCHAR(20) UNIQUE NOT NULL);

CREATE TABLE main_courses (main_course_id SERIAL PRIMARY KEY, name VARCHAR(50) UNIQUE NOT NULL, price NUMERIC (5,2));

CREATE TABLE drinks (drink_id SERIAL PRIMARY KEY, name VARCHAR(50) UNIQUE NOT NULL, price NUMERIC (5,2));

--CREATE TABLE meals (meals_id SERIAL PRIMARY KEY, meals_name VARCHAR(101), meals_price NUMERIC(6,2));

CREATE TABLE orders (order_id SERIAL PRIMARY KEY, order_date TIMESTAMP NOT NULL DEFAULT NOW(), customer_id INTEGER NOT NULL, order_sum_price numeric(6,2), FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE);

CREATE TABLE order_meal (order_id INTEGER NOT NULL, meals_id INTEGER NOT NULL, quantity INTEGER DEFAULT 1, PRIMARY KEY (order_id, meals_id), FOREIGN KEY (order_id) REFERENCES orders (order_id) ON DELETE CASCADE);

CREATE TABLE main_courses (main_course_id SERIAL PRIMARY KEY, name VARCHAR(50) NOT NULL, price NUMERIC(5,2) NOT NULL);

CREATE TABLE discounts (discount_id SERIAL PRIMARY KEY,customer_id INTEGER NULL, discount_percentage INTEGER NOT NULL, meal_id INTEGER NOT NULL, period VARCHAR(50) NOT NULL);

INSERT INTO customers (name, mail, phone) VALUES ('John Smith', 'john@gmail.com', '+38(050) 111-11-11');
INSERT INTO customers (name, mail, phone) VALUES ('Jane Doe', 'jane@gmail.com', '+38(067) 111-11-11');
INSERT INTO customers (name, mail, phone) VALUES ('Bob Johnson', 'bob@gmail.com', '+38(067) 111-11-12');
INSERT INTO customers (name, mail, phone) VALUES ('Alice Lee', 'alice@gmail.com', '+38(067) 111-11-22');
INSERT INTO customers (name, mail, phone) VALUES ('David Davis', 'david@gmail.com', '+38(067) 111-12-22');
INSERT INTO customers (name, mail, phone) VALUES ('Emily Brown', 'emily@gmail.com', '+38(067) 111-12-32');
INSERT INTO customers (name, mail, phone) VALUES ('George Williams', 'george@gmail.com', '+38(067) 111-12-52');
INSERT INTO customers (name, mail, phone) VALUES ('Hannah Miller', 'hannah@gmail.com', '+38(067) 811-12-52');
INSERT INTO customers (name, mail, phone) VALUES ('Isaac Wilson', 'isaac@gmail.com', '+38(067) 861-12-52');
INSERT INTO customers (name, mail, phone) VALUES ('Julia Garcia', 'julia@gmail.com', '+38(067) 861-42-52');
INSERT INTO customers (name, mail, phone) VALUES ('Kevin Jones', 'kevin@gmail.com', '+38(067) 871-42-52');
INSERT INTO customers (name, mail, phone) VALUES ('Laura Martinez', 'laura@gmail.com', '+38(067) 271-42-52');
INSERT INTO customers (name, mail, phone) VALUES ('Michael Rodriguez', 'michael@gmail.com', '+38(099) 233-42-52');
INSERT INTO customers (name, mail, phone) VALUES ('Natalie Davis', 'natalie@gmail.com', '+38(099) 933-42-52');
INSERT INTO customers (name, mail, phone) VALUES ('Oliver Robinson', 'oliver@gmail.com', '+38(099) 935-42-52');
INSERT INTO customers (name, mail, phone) VALUES ('Penelope Taylor', 'penelope@gmail.com', '+38(099) 935-72-52');
INSERT INTO customers (name, mail, phone) VALUES ('Quinn Johnson', 'quinn@gmail.com', '+38(099) 935-12-52');
INSERT INTO customers (name, mail, phone) VALUES ('Rachel Baker', 'rachel@gmail.com', '+38(099) 932-66-52');
INSERT INTO customers (name, mail, phone) VALUES ('Samantha Scott', 'samantha@gmail.com', '+38(099) 935-67-52');
INSERT INTO customers (name, mail, phone) VALUES ('Thomas Clark', 'thomas@gmail.com', '+38(099) 935-60-52');


INSERT INTO main_courses (name, price) VALUES ('Hamburger', 4.99);
INSERT INTO main_courses (name, price) VALUES ('Cheeseburger', 5.49);
INSERT INTO main_courses (name, price) VALUES ('Hot dog', 3.99);
INSERT INTO main_courses (name, price) VALUES ('Chicken nuggets', 6.99);
INSERT INTO main_courses (name, price) VALUES ('Fish and chips', 7.99);
INSERT INTO main_courses (name, price) VALUES ('Grilled chicken sandwich', 6.49);
INSERT INTO main_courses (name, price) VALUES ('BBQ pork sandwich', 7.49);
INSERT INTO main_courses (name, price) VALUES ('Meatballs', 6.99);
INSERT INTO main_courses (name, price) VALUES ('Spicy turkey sandwich', 5.99);
INSERT INTO main_courses (name, price) VALUES ('Taco salad', 8.99);


INSERT INTO drinks (name, price) VALUES ('Coca-Cola', 1.99);
INSERT INTO drinks (name, price) VALUES ('Sprite', 1.99);
INSERT INTO drinks (name, price) VALUES ('Fanta', 1.99);
INSERT INTO drinks (name, price) VALUES ('Dr. Pepper', 2.49);
INSERT INTO drinks (name, price) VALUES ('Lager beer', 2.49);
INSERT INTO drinks (name, price) VALUES ('Pilsner beer', 2.00);
INSERT INTO drinks (name, price) VALUES ('Iced tea', 2.49);
INSERT INTO drinks (name, price) VALUES ('Orange juice', 2.99);
INSERT INTO drinks (name, price) VALUES ('Apple juice', 2.99);
INSERT INTO drinks (name, price) VALUES ('Milkshake', 3.99);



 SELECT * INTO TABLE meals FROM (SELECT CONCAT(main_courses.name, ' + ', drinks.name) as meal_name, (main_courses.price + drinks.price) as meal_price FROM  main_courses CROSS JOIN drinks) as sub;
 
 ALTER TABLE meals ADD COLUMN meals_id SERIAL PRIMARY KEY;

 ALTER TABLE order_meal ADD CONSTRAINT  order_mealmeals_id_fkey FOREIGN KEY (meals_id) REFERENCES meals (meals_id) ON DELETE CASCADE;
 
 
 
 
 
 


--ALTER tABLE orders ADD CONSTRAINT  orders_customer_id_fkey FOREIGN KEY (customer_id) REFERENCES customers (customer_id) ON DELETE CASCADE;
