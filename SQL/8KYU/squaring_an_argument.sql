--# Solution for task: https://www.codewars.com/kata/523b623152af8a30c6000027/

--# write your SQL statement here: 
-- you are given a table 'square' with column 'n'
-- return a table with:
-- this column and your result in a column named 'res'

SELECT n, POWER(n, 2)::INT AS res
FROM square;