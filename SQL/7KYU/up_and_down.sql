SELECT 
(CASE 
 WHEN SUM(number1 % 2) <> 0 THEN MIN(number1)
 ELSE MAX(number1) 
END) as number1,
(CASE 
 WHEN SUM(number2 % 2) <> 0 THEN MIN(number2)
 ELSE MAX(number2) 
END) as number2
FROM numbers