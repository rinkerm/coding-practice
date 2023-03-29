--LANGUAGE = MS SQL
WITH ranked AS (
SELECT End_Date, DENSE_RANK() OVER(ORDER BY End_Date) dr
    FROM Projects
    GROUP BY End_Date
)
SELECT DATEADD(day,-1,min(End_Date)), max(End_Date)
from ranked
GROUP BY DATEDIFF(day,dr,End_Date)
ORDER BY DATEDIFF(d,MAX(END_DATE),DATEADD(day,-1,MIN(END_DATE))) desc, DATEADD(day,-1,MIN(END_DATE))
