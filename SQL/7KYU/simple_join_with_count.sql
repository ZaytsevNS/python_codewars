SELECT p.*, count(t.id) AS toy_count
FROM people p INNER JOIN toys t ON t.people_id = p.id 
GROUP BY p.id