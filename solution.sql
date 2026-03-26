##24/03/2026
  
select -number as res
from opposite;

SELECT CONCAT_WS(' ', prefix, first, last, suffix) AS title
FROM names;


SELECT capital
FROM countries
WHERE (continent = 'Africa' or continent = 'Afrika') 
  AND country LIKE 'E%'
ORDER BY capital
LIMIT 3;


WITH special_sales AS (
    SELECT *
    FROM sales
    WHERE price > 90
)
SELECT id, name
FROM departments
WHERE id IN (
    SELECT department_id
    FROM special_sales
);


#26/03/2026

SELECT 
    SUBSTRING(project, 1, commits) AS project,
    RIGHT(address, contributors) AS address
FROM repositories;


SELECT price * amount AS total 
FROM items;
