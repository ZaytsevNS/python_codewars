-- Solution for task: https://www.codewars.com/kata/583710ccaa6717322c000105/

SELECT "number",
  CASE
    WHEN ("number" % 2)::BOOL THEN "number" * 9
    WHEN NOT ("number" % 2)::BOOL THEN "number" * 8
  END AS res
FROM multiplication;