-- Solution for task: https://www.codewars.com/kata/54ff3102c1bad923760001f3/

SELECT str, (LENGTH(str) - LENGTH(TRANSLATE(LOWER(str), 'aeiou', '')))::INT AS res
FROM getcount;