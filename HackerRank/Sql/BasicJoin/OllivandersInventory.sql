--LANGUAGE = MS SQL

WITH ranked (id, code, coins_needed, power, rank)
as (
    SELECT w.id,
    w.code,
    w.coins_needed,
    w.power,
    ROW_NUMBER() OVER (PARTITION BY w.code, w.power ORDER BY coins_needed asc) as rank
    FROM Wands w
)

SELECT w.id, wp.age, w.coins_needed, w.power
FROM ranked w join Wands_Property wp on w.code = wp.code 
WHERE wp.is_evil = 0
and w.rank = 1
ORDER BY w.power desc, wp.age desc

