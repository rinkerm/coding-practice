--LANGUAGE = MS SQL
WITH top_scores(challenge_id,top_score)
as (
    SELECT c.challenge_id,
            d.score as top_score
    FROM Challenges c join Difficulty d on c.difficulty_level = d.difficulty_level
)
, has_max(hacker_id, no_maxed)
as (
        SELECT s.hacker_id,
        COUNT(s.challenge_id) as no_maxed
        FROM Submissions s join top_scores ts on s.challenge_id = ts.challenge_id
        WHERE s.score = ts.top_score
        GROUP BY s.hacker_id
)
SELECT hm.hacker_id, h.name
from has_max hm join Hackers h on hm.hacker_id = h.hacker_id
WHERE hm.no_maxed > 1
ORDER BY hm.no_maxed desc, hm.hacker_id
