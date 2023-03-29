--LANGUAGE = MS SQL

WITH CTE([Actor],[Doctor],[Professor],[Singer], cr)
as
(
   SELECT 
      CASE when [Occupation]='Actor' then Name end,
      CASE when [Occupation]='Doctor' then Name end,
      CASE when [Occupation]='Professor' then Name end,
      CASE when [Occupation]='Singer' then Name end,
    ROW_NUMBER() over (PARTITION BY OCCUPATION ORDER BY NAME) as cr
   FROM OCCUPATIONS
)
SELECT MAX(CTE.[Doctor]), 
	MAX(CTE.[Professor]), 
	MAX([Singer]), 
	MAX([Actor]) 
from CTE 
GROUP BY cr
