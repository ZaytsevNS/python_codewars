-- Solution for task: https://www.codewars.com/kata/57a1fd2ce298a731b20006a4/

SELECT str, (LOWER(str) = REVERSE(LOWER(str)))::BOOL AS res 
FROM ispalindrome;
