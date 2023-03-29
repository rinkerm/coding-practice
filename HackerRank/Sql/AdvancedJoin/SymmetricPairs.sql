--LANGUAGE = MS SQL
WITH indexed (X,Y,rowno)
as (SELECT X,
        Y,
        ROW_NUMBER() OVER(ORDER BY X) as rowno
   FROM Functions)
,
pairs (X,Y, rowno)
as (SELECT a.X, 
        a.Y, 
        ROW_NUMBER() OVER(PARTITION BY a.X, a.Y ORDER BY a.X) as rowno
    FROM indexed a 
        JOIN indexed b on a.X = b.Y 
            and b.X = a.Y 
            and a.rowno <> b.rowno
    WHERE a.X <= a.Y)

SELECT X,Y
from pairs
WHERE rowno = 1
ORDER BY X

