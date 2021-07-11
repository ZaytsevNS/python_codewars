SELECT d.id, d.name
FROM departments d
WHERE d.id IN (SELECT s.department_id FROM sales s WHERE s.price > 98.00);