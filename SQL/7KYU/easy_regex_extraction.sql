SELECT name, greeting, (regexp_matches(greeting, '#(\d+)'))[1] AS user_id 
FROM greetings;