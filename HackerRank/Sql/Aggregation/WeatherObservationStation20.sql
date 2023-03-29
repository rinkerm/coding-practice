--LANGUAGE = MySQL
SELECT ROUND(LAT_N,4)
FROM 
    (SELECT LAT_N, 
        row_number() over (ORDER BY LAT_N) as rowno 
     from STATION) ordered
JOIN 
    (SELECT CEIL(COUNT(ID)/2) as num 
     FROM STATION) counted 
on ordered.rowno = num
