SELECT m.id, m.name, split_part(m.characteristics, ',', 1) AS characteristic
FROM monsters m
ORDER BY id