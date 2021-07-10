SELECT p.id, p.name, p.stock 
FROM products p 
WHERE p.stock <= 2 AND p.producent = 'CompanyA' 
ORDER BY p.id