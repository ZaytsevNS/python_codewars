-- Solution for task: https://www.codewars.com/kata/59491429952ac97ad9000106/

SELECT 
  LENGTH(number1::TEXT) AS octnum1,
  LENGTH(number2::TEXT) AS octnum2,
  LENGTH(number3::TEXT) AS octnum3,
  LENGTH(number4::TEXT) AS octnum4,
  LENGTH(number5::TEXT) AS octnum5
FROM numbers;