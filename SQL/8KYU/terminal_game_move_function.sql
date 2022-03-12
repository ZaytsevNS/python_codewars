--# write your statement here: you will be given a table 'moves' with columns 'position' and 'roll'. return a table with a column 'res'. #--
SELECT (2 * roll + position) AS res
FROM moves