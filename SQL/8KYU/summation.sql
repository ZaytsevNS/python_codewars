--# Solution for task: https://www.codewars.com/kata/55d24f55d7dd296eb9000030/

--# write your SQL statement here: you are given a table 'kata' with a column 'n', return a table with 'n' and your result stored in a column naed 'res'.
SELECT n, n*(n+1)/2 AS res
FROM kata;