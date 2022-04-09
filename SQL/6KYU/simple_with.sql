WITH special_sales (id, name)
    AS
    (
        SELECT DISTINCT d.id, d.name FROM departments d
        LEFT JOIN sales s ON d.id = s.department_id
        WHERE s.price > 90
    )
SELECT * FROM special_sales ORDER BY id