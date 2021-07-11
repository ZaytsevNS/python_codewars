SELECT c.customer_id, c.email, sum(cast(p.amount as float)) as total_amount, count(p.customer_id) as payments_count
FROM customer c
INNER JOIN payment p ON p.customer_id = c.customer_id GROUP BY c.customer_id 
ORDER BY total_amount DESC
LIMIT 10