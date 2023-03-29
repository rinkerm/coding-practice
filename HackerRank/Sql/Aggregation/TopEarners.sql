--LANGUAGE MySQL
SELECT income, 
	COUNT(employee_id)
From Employee
JOIN
	(SELECT MAX(months * salary) as income
	FROM Employee) maxxed 
on months*salary = income
GROUP BY income
