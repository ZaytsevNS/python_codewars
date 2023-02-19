-- Solution for task: https://www.codewars.com/kata/5545f109004975ea66000086/

SELECT id, (MOD(n, x) = 0 AND MOD(n, y) = 0)::BOOL AS res
FROM kata;
