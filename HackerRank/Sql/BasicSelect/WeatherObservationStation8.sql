--LANGUAGE = MySQL
SELECT DISTINCT CITY
FROM STATION
WHERE RIGHT(CITY,1) in ('a','e','i','o','u')
and LEFT(CITY,1) in ('a','e','i','o','u')