--LANGUAGE = MySQL
SELECT Case when AB+AC+CB = 3 and tri = 1 then "Equilateral"
            when AB+AC+CB = 1 and tri = 1 then "Isosceles"
            when AB+AC+CB = 0 and tri = 1 then "Scalene"
            else "Not A Triangle" end as ans
FROM
	(SELECT Case when A=B then 1 else 0 end as AB,
		Case when A=C then 1 else 0 end as AC, 
		Case when C=B then 1 else 0 end as CB, 
		Case when A+B >C then 1 else 0 end as tri
	FROM TRIANGLES) logic
