-- Check the columns of a dataset 
PRAGMA table_info(indian_startup_funding)

-- 1. Write SQL query to sum all the funding AmountinUSD, where City location equals “Bengaluru”
SELECT SUM(`Amount in USD`) 
FROM indian_startup_funding 
WHERE `City  Location`='Bengaluru'

-- 2. Write SQL query to sort the table by startup name DESC
SELECT *
FROM indian_startup_funding
ORDER BY UPPER(`Startup Name`) DESC

-- 3. Write SQL query to sum all the funding Amount in USD, where City location equals “Bengaluru” and Amount in USD>38000
SELECT SUM(`Amount in USD`) 
FROM indian_startup_funding
WHERE `City  Location`='Bengaluru'
      AND `Amount in USD`>380000
	  
-- 4. Write SQL query to get all CityLocations that has an Amount in USD >380000
SELECT `City  Location`
FROM indian_startup_funding
WHERE `Amount in USD`>380000

-- 5. Write SQL query to get only unique City Locations that has an Amount in USD >380000
SELECT DISTINCT `City  Location`
FROM indian_startup_funding
WHERE `Amount in USD`>380000

-- 6. Write SQL query to get all Startup Names where Amount in USD<380000
SELECT  `Startup Name`
FROM indian_startup_funding
WHERE `Amount in USD`<380000

-- 7. Write SQL query to sort the output from the previous question DESC
SELECT  `Startup Name`
FROM indian_startup_funding
WHERE `Amount in USD`<380000
ORDER BY `Startup Name` DESC

-- 8. Write SQL query to get the City location that has the maximum funding amount “Note that is the data is not cleaned properly you will get non logical result”
-- Solution 1: Using LIMIT
-- Time processing 5ms
SELECT `City  Location`
FROM indian_startup_funding
ORDER BY `Amount in USD` DESC
LIMIT 1

-- Solution 2: Using SUB-QUERIE, MAX
-- Time processing 6ms
SELECT `City  Location`
FROM indian_startup_funding
WHERE `Amount in USD` = (SELECT MAX(`Amount in USD`) FROM indian_startup_funding)

-- 9. Write SQL query to get the total funding Amount in USD for each Industry Vertical
SELECT `Industry Vertical`, 
		SUM(`Amount in USD`)
FROM indian_startup_funding
GROUP BY `Industry Vertical`

-- 10. Write SQL query to get the total funding Amount in USD for each Industry Vertical that starts with letter “A”
SELECT `Industry Vertical`, 
		SUM(`Amount in USD`)
FROM indian_startup_funding
WHERE `Industry Vertical` LIKE 'A%'
GROUP BY `Industry Vertical`

-- 11. Write SQL query to get the total funding Amount in USD for each Industry Vertical that starts with letter “A” and sort the output DESC by the total AmountinUSD
SELECT `Industry Vertical`, 
		SUM(`Amount in USD`)
FROM indian_startup_funding
WHERE `Industry Vertical` LIKE 'A%'
GROUP BY `Industry Vertical`
ORDER BY SUM(`Amount in USD`) DESC

-- 12. Write SQL query to count all the start_ups in the Education field
SELECT COUNT(`Startup Name`)
FROM indian_startup_funding
WHERE `Industry Vertical`='Education'

-- 13. Write SQL query to count all the start_Ups in the E-Commerce field
SELECT COUNT(`Startup Name`)
FROM indian_startup_funding
WHERE `Industry Vertical`='E-Commerce'

-- 14. Write SQL query to count all the start_Ups in the E-Commerce field, where city location equals “Bengaluru”
SELECT COUNT(`Startup Name`)
FROM indian_startup_funding
WHERE `Industry Vertical`='E-Commerce'
      AND `City  Location`='Bengaluru'
	  
-- 15. For each Industry Vertical find the total funding amount
SELECT `Industry Vertical`, 
		SUM(`Amount in USD`)
FROM indian_startup_funding
GROUP BY `Industry Vertical`

-- 16. For each Industry Vertical find the total funding amount as “Total_fund” and the average funding amount as “Avg_Fund”. In this question provide two answer 1- using group by Industry Vertical, 2- using sub_queries
-- Solution 1: using group by Industry Vertical
SELECT `Industry Vertical`, 
		SUM(`Amount in USD`) as 'Total_Fund',
		AVG(`Amount in USD`) AS 'Avg_Fund'
FROM indian_startup_funding
GROUP BY `Industry Vertical`
ORDER BY `Industry Vertical`

-- Solution 2: using sub queries
SELECT DISTINCT
    `Industry Vertical`,
    (
        SELECT SUM(isf2.`Amount in USD`)
        FROM indian_startup_funding isf2
        WHERE isf2.`Industry Vertical` = isf.`Industry Vertical`
    ) AS Total_Fund,
    (
        SELECT AVG(isf3.`Amount in USD`)
        FROM indian_startup_funding isf3
        WHERE isf3.`Industry Vertical` = isf.`Industry Vertical`
    ) AS Avg_Fund
FROM indian_startup_funding isf
ORDER BY `Industry Vertical`

-- 17. Write SQL query to get the minimum value of funding for the “Uniphore” start_up
SELECT MIN(`Amount in USD`)
FROM indian_startup_funding
WHERE `Startup Name`='Uniphore'

-- 18. Write SQL query to get the length of the city location names
SELECT `City  Location`, 
		LENGTH(`City  Location`)
FROM indian_startup_funding

-- 19. Write SQL query to convert start_ups names into uppercase if the funding amount is >380,000
SELECT UPPER(`Startup Name`)
FROM indian_startup_funding
WHERE `Amount in USD`>380000

-- 20. Write SQL query to select distinct industry vertical names, knowing that names are mix of lowercase and uppercase values.
SELECT DISTINCT UPPER(`Industry Vertical`)
FROM indian_startup_funding
ORDER BY UPPER(`Industry Vertical`)
