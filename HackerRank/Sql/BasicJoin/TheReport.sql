--LANGUAGE = MS SQL
SELECT Case when Grade >= 8 then Name else Null end, 
	Grade, 
	Marks
FROM Students 
	join Grades on Marks >= Min_Mark and Marks <= Max_Mark
ORDER BY Grade desc, 
	Case when Grade >= 8 then Name end,
	Case when Grade < 8 then Marks end

