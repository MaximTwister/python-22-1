--5. Calculate the average order value (during all the time)

with basic as (
SELECT o.id as order_id,
 case when dis.period @> o.order_date and dis.meal_id is not null then ((mc.price + d.price)*om.portions * (100 - dis.percents)/100)::numeric(10,2)
       when d2.period @> o.order_date and d2.customer_id  is not null then ((mc.price + d.price)*om.portions * (100 - d2.percents)/100)::numeric(10,2)
       else (mc.price + d.price)*om.portions
       end sum_disc
FROM meals m
join main_courses mc on mc.id = m.main_course_id
join drinks d on d.id = m.drink_id
join order_meal om on m.id = om.meal_id
join orders o on om.order_id = o.id
join customers c on c.id = o.customer_id
left join discounts dis on dis.meal_id = m.id
left join discounts d2 on d2.customer_id = c.id
WHERE o.order_date BETWEEN '2023-01-01' AND '2023-04-01'
order by o.order_date)

select AVG(sum_disc)::numeric(10,2) AS AVG
FROM basic;