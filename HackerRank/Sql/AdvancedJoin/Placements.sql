--LANGUAGE = MS SQL
SELECT s.Name
FROM Students s join Friends f on s.ID = f.ID
join Packages own on own.ID = s.ID
join Packages other on other.ID = f.Friend_ID
WHERE own.Salary < other.Salary
ORDER BY other.Salary
