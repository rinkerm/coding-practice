--LANGUAGE = MySQL
SELECT c.company_code, 
		c.founder, 
		COALESCE(lm.lmno,0), 
		COALESCE(sm.smno,0), 
		COALESCE(m.mno,0), 
		COALESCE(e.eno,0)

FROM Company c left join
	(SELECT COUNT(DISTINCT lead_manager_code) as lmno, 
	company_code
	FROM Lead_Manager
	GROUP BY company_code) lm 
on lm.company_code = c.company_code left join 
	(SELECT COUNT(DISTINCT senior_manager_code) as smno, 
	company_code
	from Senior_Manager
	GROUP BY company_code) sm 
on sm.company_code = c.company_code left join
	(SELECT COUNT(DISTINCT manager_code) as mno, 
	company_code 
 	FROM Manager
 	GROUP BY company_code) m 
 on m.company_code = c.company_code left join 
	(SELECT COUNT(DISTINCT employee_code) as eno, 
	company_code
 	FROM Employee
 	GROUP BY company_code) e 
on e.company_code = c.company_code
ORDER BY c.company_code asc

