SELECT SUM(amount) FROM expenses;

SELECT category,SUM(amount) FROM expenses
GROUP BY category;

SELECT EXTRACT(month from expense_date) AS month_of_year,
SUM(amount)
FROM expenses
GROUP BY month_of_year
ORDER BY month_of_year;

SELECT *
FROM expenses
WHERE amount =(SELECT MAX(amount) FROM expenses)
ORDER BY expense_date;

