--LANGUAGE = MS SQL
SELECT N, 
	CASE WHEN a.P Is Null then 'Root'
	WHEN exists (
					SELECT 1 
					from BST b 
					where b.P = a.N
				) then 'Inner'
	Else 'Leaf' END
FROM BST a
ORDER BY a.N
