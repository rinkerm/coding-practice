--LANGUAGE = MySQL
SELECT total - cities
FROM (SELECT COUNT(ID) as total FROM STATION) totes join

(SELECT COUNT(city) as cities 
 FROM 
    (SELECT DISTINCT CITY as city
     FROM STATION
    ) distincted
) c on 1=1
