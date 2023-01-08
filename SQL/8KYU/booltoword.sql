-- # Solution for task: https://www.codewars.com/kata/53369039d7ab3ac506000467/
-- # write your SQL statement here: you are given a table 'booltoword' with column 'bool', return a table with column 'bool' and your result in a column named 'res'.

SELECT bool,
  CASE
    WHEN bool = true THEN 'Yes'
    WHEN bool = false THEN 'No'
  END AS res
FROM booltoword;