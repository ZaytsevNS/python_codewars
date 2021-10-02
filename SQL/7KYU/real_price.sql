SELECT name, weight, price, ROUND(CAST(price / weight * 1000 AS NUMERIC), 2)::FLOAT AS price_per_kg 
FROM products
ORDER BY price_per_kg, name ASC
