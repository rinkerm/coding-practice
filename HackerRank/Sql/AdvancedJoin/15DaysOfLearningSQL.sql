--Language  = MS SQL
WITH ranked (id, dt, dr) 
AS (SELECT distinct hacker_id as id, 
    submission_date as dt, 
    ROW_NUMBER() OVER(PARTITION BY hacker_id ORDER BY submission_date) as dr
    FROM Submissions
    GROUP BY hacker_id, submission_date

),
counted(dt, counts)
AS (
SELECT dt, COUNT(id)
from ranked
Where DATEDIFF(day,dr,dt) = (SELECT MIN(DATEDIFF(day,dr,dt)) FROM ranked )
GROUP BY dt
)
,hacker_sums (id,dt,summed)
AS (SELECT MIN(hacker_id),
            submission_date,
            summed
    FROM (SELECT hacker_id, 
            submission_date, 
            COUNT(submission_id) as summed
    FROM Submissions 
    GROUP BY submission_date, 
        hacker_id) temp
   GROUP BY submission_date, summed)
,
maxed (dt,num)
AS (
    SELECT dt, MAX(summed) as num
    from hacker_sums
    GROUP BY dt
)

SELECT c.dt, c.counts, h.hacker_id, h.name
from counted c join maxed m on c.dt = m.dt
join hacker_sums s on s.dt = m.dt and s.summed = m.num
join Hackers h on h.hacker_id = s.id
ORDER BY dt

