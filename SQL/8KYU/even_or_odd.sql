SELECT (CASE WHEN (number % 2) <> 0 THEN 'Odd'
ELSE 'Even' END) is_even FROM numbers