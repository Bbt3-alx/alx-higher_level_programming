-- a script that prints the full description of the table first_table from the database hbtn_0c_0 in mysql server
SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_KEY, COLUMN_DEFAULT, EXTRA
FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA = (SELECT DATABASE()) AND TABLE_NAME = 'first_table'
