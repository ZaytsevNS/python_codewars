SELECT capital FROM countries
WHERE continent in ('Africa', 'Afrika') and country LIKE 'E%'
ORDER BY capital LIMIT 3
