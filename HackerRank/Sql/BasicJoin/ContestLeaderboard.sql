--LANGUAGE = MySQL
SELECT h.hacker_id, 
	h.name, 
	scores.total
FROM Hackers h 
	join 
		(SELECT hacker_id, 
			SUM(max_score) as total 
		from 
			(SELECT hacker_id, 
				challenge_id, 
				MAX(score) as max_score 
			from Submissions 
			GROUP BY hacker_id, 
				challenge_id) sub_scores 
			where max_score > 0 
			group by hacker_id) scores 
	on h.hacker_id = scores.hacker_id
where scores.total > 0
ORDER BY scores.total desc, h.hacker_id
