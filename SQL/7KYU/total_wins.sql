SELECT name, SUM(won) AS won, SUM(lost) AS lost
FROM fighters
JOIN winning_moves ON winning_moves.id = fighters.move_id
WHERE move NOT IN ('Hadoken', 'Shouoken', 'Kikoken')
GROUP BY name
ORDER BY won DESC LIMIT 6
