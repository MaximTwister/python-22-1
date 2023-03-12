--4. Find the customer who has placed the maximum number of orders.

 select customer_id, num
 from(
     select customer_id,
           num,
           DENSE_RANK() OVER (ORDER BY num desc) AS DENSE_RANK
           from (select o.customer_id,
     count (o.id) as num
     from orders o
     group by o.customer_id
     order by count (o.id) desc)v)k
     where dense_rank  = 1;