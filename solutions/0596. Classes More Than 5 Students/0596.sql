SELECT class
FROM Courses
GROUP BY 1
HAVING COUNT(*) >= 5;
