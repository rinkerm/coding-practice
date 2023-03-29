--LANGUAGE = MySQL
SELECT name
from employee
where salary > 2000
and months < 10
ORDER BY employee_id asc
