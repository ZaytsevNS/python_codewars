CREATE FUNCTION increment(age INTEGER) RETURNS INTEGER AS
'BEGIN
  RETURN age + 1;
END;'
LANGUAGE plpgsql;