-- Solution for task: https://www.codewars.com/kata/5943a58f95d5f72cb900006a/

SELECT LEFT(project, commits) AS project, RIGHT(address, contributors) AS address
FROM repositories;
