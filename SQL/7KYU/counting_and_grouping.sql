SELECT race, count(race) AS count 
FROM demographics 
GROUP BY race ORDER BY race DESC