--# Solution for task: https://www.codewars.com/kata/5ce9c1000bab0b001134f5af/

--# write your SQL statement here: you are given a table 'quarterof' with column 'month', return a table with column 'month' and your result in a column named 'res'.

SELECT month,
  CASE
    WHEN month BETWEEN 1 AND 3 THEN 1
    WHEN month BETWEEN 4 AND 6 THEN 2
    WHEN month BETWEEN 7 AND 9 THEN 3
    WHEN month BETWEEN 10 AND 12 THEN 4
  END AS res
FROM quarterof