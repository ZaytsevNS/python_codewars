SELECT 
  CHAR_LENGTH(name::text) AS id,
  CHAR_LENGTH(legs::text) AS name,
  CHAR_LENGTH(arms::text) AS legs,
  CHAR_LENGTH(characteristics::text) AS arms,
  CHAR_LENGTH(id::text) AS characteristics
FROM monsters