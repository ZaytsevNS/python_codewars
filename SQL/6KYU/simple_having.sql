SELECT age, count(age) AS total_people
FROM people
GROUP BY age
HAVING count(age) >= 10