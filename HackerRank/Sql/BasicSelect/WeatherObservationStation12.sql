--LANGUAGE = MySQL
SELECT DISTINCT CITY
FROM STATION
WHERE RIGHT(CITY,1) not in ('a','e','i','o','u')
and LEFT(CITY,1) not in ('a','e','i','o','u')
