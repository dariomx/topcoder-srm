/* Write your PL/SQL query statement below */
SELECT FirstName, LastName, City, State
FROM Person p LEFT JOIN Address a
USING (PersonId);
