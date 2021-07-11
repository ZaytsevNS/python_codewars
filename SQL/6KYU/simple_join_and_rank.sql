SELECT p.*, count(s.sale) AS sale_count, RANK() OVER(PARTITION BY p.id ORDER BY p.id DESC) AS sale_rank
FROM people p
INNER JOIN sales s ON p.id = s.people_id
GROUP BY p.id