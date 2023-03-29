--LANGUAGE = MS SQL
with vs (challenge_id, tv, tuv)
as (
    SELECT challenge_id as challenge_id,
        SUM(total_views) as tv,
        SUM(total_unique_views) as tuv
    FROM View_Stats
    GROUP BY challenge_id
),
ss (challenge_id, ts, tas)
as (
    SELECT challenge_id,
        SUM(total_submissions) as ts,
        SUM(total_accepted_submissions) as tas
    FROM Submission_Stats
    GROUP BY challenge_id
)

SELECT c.contest_id, c.hacker_id, c.name, SUM(ss.ts), SUM(ss.tas),SUM(vs.tv), SUM(vs.tuv)
FROM Contests c join Colleges col on c.contest_id = col.contest_id 
join Challenges chal on col.college_id = chal.college_id
left join ss on chal.challenge_id = ss.challenge_id left join vs on chal.challenge_id = vs.challenge_id
GROUP BY c.contest_id, c.hacker_id, c.name
HAVING SUM(ss.ts) <> 0 and SUM(ss.tas) <> 0 and SUM(vs.tv) <> 0 and SUM(vs.tuv) <> 0
ORDER BY c.contest_id
