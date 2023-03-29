--LANGUAGE = MS SQL
WITH ranked([hacker_id],[counted], [maxed], [cr])
as 
    (
        SELECT hacker_id, 
        COUNT(challenge_id) as counted, 
        MAX(COUNT(challenge_id)) OVER() as maxed,
        ROW_NUMBER() OVER (PARTITION BY COUNT(hacker_id) ORDER BY hacker_id) as cr 
        FROM Challenges
        GROUP BY hacker_id)
        
SELECT r.hacker_id, 
	h.name, 
	r.counted 
from ranked r 
	join Hackers h on r.hacker_id = h.hacker_id
WHERE r.counted not in 
	(SELECT r1.counted 
	from ranked r1 
	WHERE r1.counted < r1.maxed and r1.cr > 1)
ORDER BY r.counted desc, r.hacker_id

