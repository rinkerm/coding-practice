--LANGUAGE = MS SQL
DECLARE @numbers Table (num INT)

DECLARE @ret AS VARCHAR(2000) = '2'

DECLARE @i AS INT = 3

INSERT INTO @numbers
SELECT 2

WHILE @i < 1001
    BEGIN
        IF NOT EXISTS(select num from @numbers where @i % num = 0)
            SET @ret = CONCAT(@ret,'&',CAST(@i AS VARCHAR(8)))
        INSERT INTO @numbers
        SELECT @i
        
        SET @i = @i + 1
    END
SELECT LEFT(@ret,len(@ret))
    
