-- Solution for task: https://www.codewars.com/kata/5763bb0af716cad8fb000580/

SELECT n,
  CASE
    WHEN n = 0 THEN n + 1
    WHEN n > 0 THEN (6 * POWER(n, 2) + 2)::INTEGER
  END AS res
FROM squares;
